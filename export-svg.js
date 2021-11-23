const fs = require("fs");
const path = require("path");
const svgo = require('svgo');
fs.readdirSync('src').forEach(f => {
    if (!f.startsWith('_') && path.extname(f) === '.svg') {
        const id = path.basename(f, '.svg');
        const src = `src/${f}`;
        const out = `out/${id}.svg`;
        const srcStr = fs.readFileSync(src).toString();
        var result = svgo.optimize(srcStr, {
            multipass: true,
            plugins: [
                {
                    name: 'preset-default',
                    params: {},
                },
            ]
        });
        const outStr = result.data.toString();
        fs.writeFileSync(out, outStr);
        console.log(out + ':' + out, srcStr.length + ':' + outStr.length, Math.floor((outStr.length / srcStr.length * 100)) + '%');
    }
});
