const fs = require("fs");
const path = require("path");
const ARMSDK = process.env['ARMSDK'];
if(!ARMSDK) {
    process.stdout.write('ARMSDK environment variable not set\n')
    process.exit(1);
}
fs.readdirSync('out').forEach(f => {
    if(path.extname(f)==='.png') {
        fs.copyFileSync('out/'+f, ARMSDK+'/armory/blender/arm/custom_icons/'+f);
    }
});
