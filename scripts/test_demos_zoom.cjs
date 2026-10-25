// Regression: a zoom click must not reach the dialog's outside-click handler.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const listeners = {};
const classes = new Set();
const dialog = {
  open: true,
  classList: {
    toggle(name) {
      if (classes.has(name)) { classes.delete(name); return false; }
      classes.add(name); return true;
    },
    remove(name) { classes.delete(name); }
  },
  addEventListener(name, fn) { listeners['dialog:' + name] = fn; }
};
const button = {
  attributes: {},
  addEventListener(name, fn) { listeners['button:' + name] = fn; },
  setAttribute(name, value) { this.attributes[name] = value; }
};
const document = {
  querySelector(selector) { return selector === 'dialog' ? dialog : button; },
  querySelectorAll() { return []; }
};
vm.runInNewContext(fs.readFileSync('demos/js/accesibilidad.js', 'utf8'), { document });
function clickZoom() {
  let stopped = false;
  listeners['button:click']({ stopPropagation() { stopped = true; } });
  // A changed dialog rectangle can exclude the original pointer position.
  if (!stopped) dialog.open = false;
}
clickZoom();
assert.equal(dialog.open, true);
assert.equal(button.attributes['aria-pressed'], 'true');
clickZoom();
assert.equal(dialog.open, true);
assert.equal(button.attributes['aria-pressed'], 'false');
listeners['dialog:close']();
assert.equal(classes.has('is-zoomed'), false);
console.log('PASS: zoom/reduce do not bubble into outside-close; close resets state.');
