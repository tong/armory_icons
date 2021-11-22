const fs = require("fs");
const path = require("path");
const svgexport = require('svgexport');
fs.readdirSync('src').forEach(f => {
    var id = path.basename(f, '.svg');
    var src ='src/' + f;1
    var out = 'out/' + id + '.png';
    svgexport.render(
        { input: src, output: out, },
        () => {
            console.log('Exported '+src+' → '+out);
        }
    );
});
