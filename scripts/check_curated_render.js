#!/usr/bin/env node
// Execute the repository's own Markdown parser offline. This is not browser QA.
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const root = path.resolve(__dirname, '..');
const source = fs.readFileSync(path.join(root, 'site/lesson.html'), 'utf8');
const parser = source.slice(source.indexOf('      function parseMd(md)'), source.indexOf('      function initCodeCopy()'));
const helpers = ['escapeHtml', 'escapeAttr'].map(name => {
  const start = source.indexOf('      function ' + name + '(');
  const end = source.indexOf('\n      }', start) + '\n      }'.length;
  if (start < 0 || end < start) throw new Error('Parser helper not found: ' + name);
  return source.slice(start, end);
}).join('\n');
// Minimal text-node escaping shim only; no layout, event loop or browser simulation.
const context = {document:{createElement(){return {
  value:'', set textContent(value){this.value=String(value);},
  get innerHTML(){return this.value.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;');}
};}}};
vm.runInNewContext(parser + '\n' + helpers, context, {timeout: 1000, filename:'site/lesson.html#offline-parser'});
const paths = process.argv.slice(2);
if (!paths.length) {console.error('Pass one or more curated zh.md paths'); process.exit(2);}
let failed = false;
for (const supplied of paths) {
  const full = path.resolve(root, supplied);
  if (!full.startsWith(root + path.sep)) throw new Error('Path outside checkout');
  const text = fs.readFileSync(full, 'utf8');
  const html = context.parseMd(text);
  const headings = Array.from(html.matchAll(/<h([1-6]) id="([^"]*)"[^>]*>(.*?)<\/h\1>/g), x => ({level:Number(x[1]),id:x[2],text:x[3]}));
  const empty = headings.filter(h => !h.id).map(h=>h.text);
  const ids = headings.map(h=>h.id);
  const duplicates = ids.filter((id,index) => id && ids.indexOf(id)!==index);
  const report = {
    file:supplied, parser_executed:true, html_bytes:Buffer.byteLength(html),
    tables:(html.match(/<table>/g)||[]).length,
    code_blocks:(html.match(/<pre>/g)||[]).length,
    figures:(html.match(/class="lesson-figure"/g)||[]).length,
    mermaid_sources:(html.match(/class="mermaid mermaid-source"/g)||[]).length,
    empty_heading_ids:empty, duplicate_heading_ids:[...new Set(duplicates)],
    browser_verified:false,
    result:empty.length||duplicates.length?'BLOCKED_SOURCE_RENDERER':'STRUCTURE_ONLY'
  };
  if (!html.includes('<h1') || !/[\u4e00-\u9fff]/.test(html)) {report.result='FAIL';failed=true;}
  console.log(JSON.stringify(report));
}
if (failed) process.exit(1);
