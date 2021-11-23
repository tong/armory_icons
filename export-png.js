const fs = require("fs");
const path = require("path");
const svgexport = require('svgexport');
fs.readdirSync('out').forEach(f => {
    if (!f.startsWith('_') && path.extname(f) === '.svg') {
        const id = path.basename(f, '.svg');
        const src = `src/${f}`;
        const out = `out/${id}.png`;
        svgexport.render({ input: src, output: out },
            () => {
                console.log(`Exported ${src} → ${out}`);
            }
        );
    }
});
