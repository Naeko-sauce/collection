 const _0xac6194 = require('crypto-js');
 window = {}
 window.indexcode = {
      'getResCode': function () {
        var _0xf80ab6 = _0xac6194.AES.encrypt(_0xac6194.enc.Utf8.parse(Math.floor(new Date().getTime() / 1000)), _0xac6194.enc.Utf8.parse("1234567887654321"), {
          'iv': _0xac6194.enc.Utf8.parse("1234567887654321"),
          'mode': _0xac6194.mode.CBC,
          'padding': _0xac6194.pad.Pkcs7
        });
        return _0xac6194.enc.Base64.stringify(_0xf80ab6.ciphertext);
      }.bind().bind()
    };
    // console.log(window.indexcode.getResCode());
    