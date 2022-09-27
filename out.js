/**
 * @fileoverview 篡改上海电力大学入校码/离校码
 *
 * @supported FUCK-SUEP
 */


var body = $response.body;

body = body.replace('hibit', 'out')

$done(body);
