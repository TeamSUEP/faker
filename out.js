/**
 * @fileoverview 篡改上海电力大学入校码/离校码
 *
 * @supported FUCK-SUEP
 */


var body = $response.body;
var url = $request.url;
if (url.indexOf('lxRedirect.jsp') !== -1) {
    body = body.replace('hibit', 'out')
} else if (url.indexOf('fxRedirect.jsp') !== -1) {
    body = body.replace('hibit', 'enter')
}

$done(body);
