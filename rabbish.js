function isSingleInstanceProd(s) {
    var i = ["mn", "ma", "im_hi", "xw", "search_aichat"];
    return ("|" + i.join("|") + "|").indexOf("|" + s + "|") > -1
}

function isLoginInstance(s) {
    return s = s || "login", s + "" == "login"
}

function saveInitInstance(s) {
    window._pass_popinit_instance = s
}

function getInitInstance() {
    return window._pass_popinit_instance
}
var passport = passport || window.passport || {};
passport._modulePool = passport._modulePool || {}, passport._define = passport._define || function(s, i) {
    passport._modulePool[s] = i && i()
}, passport._getModule = passport._getModule || function(s) {
    return passport._modulePool[s]
}, window.upsmsStore = {
    reg_upsms: "106929130003000002",
    verify_upsms: "106929130003000004",
    verify_text_upsms: "1069 2913 0003 000 004"
}, window.YY_TPL_CONFIG = "yylive,yyliveserver,yyanchor,pcyy,yyudbsec,bdgameassist,yoyuyin,";
try {
    if (window.localStorage && window.localStorage.getItem("upsms-pcApi")) try {
        window.upsmsStore = JSON.parse(window.localStorage.getItem("upsms-pcApi"))
    } catch (e) {}
} catch (e) {}
var passport = window.passport || {};
passport.pop = passport.pop || {}, passport.pop.insertScript = passport.pop.insertScript || function(s, i) {
    var n = document,
        a = n.createElement("SCRIPT");
    a.type = "text/javascript", a.charset = "UTF-8", a.readyState ? a.onreadystatechange = function() {
        ("loaded" === a.readyState || "complete" === a.readyState) && (a.onreadystatechange = null, i && i())
    } : a.onload = function() {
        i && i()
    }, a.src = s, n.getElementsByTagName("head")[0].appendChild(a)
}, passport.ieVersion = function() {
    var s;
    try {
        var i = navigator.userAgent.toLowerCase(),
            n = i.indexOf("msie") > -1;
        n && i.match(/msie ([\d.]+)/) && (s = i.match(/msie ([\d.]+)/)[1])
    } catch (a) {
        s = 0
    }
    return s
}, passport.pop.init = passport.pop.init || function(s) {
    var i = {
        "http:": "http://ppui-static-pc.cdn.bcebos.com",
        "https:": "https://ppui-static-pc.cdn.bcebos.com"
    };
    if (passport.ieVersion() <= 8 && (i = {
            "http:": "http://passport.baidu.com",
            "https:": "https://passport.baidu.com"
        }), isSingleInstanceProd(s.apiOpt.product) && isLoginInstance(s.type) && getInitInstance()) return getInitInstance();
    var n;
    n = s && "https" === s.protocol ? "https:" : window.location ? window.location.protocol.toLowerCase() : document.location.protocol.toLowerCase();
    var a, e, t, p = ["pp", "mn", "wk", "cmovie", "translate", "baidugushitong", "ik", "exp", "waimai", "jn", "im", "do", "yuedu", "hao123", "tb", "netdisk", "developer", "newdev", "image_eco", "zbsc", "bpit_hcm", "defensor", "study", "bizcrm", "sjhlexus_all", "zhengxin"],
        c = s && s.apiOpt && s.apiOpt.product || "",
        o = ("|" + p.join("|") + "|").indexOf("|" + c + "|") > -1 || "v4" === (s && s.loginVersion),
        _ = "v5" === (s && s.loginVersion);
    _ ? (a = "/passApi/js/uni_loginv4_cf6db29.js", e = "/passApi/js/uni_loginv4_tangram_ce65df7.js", t = "/passApi/css/uni_loginv5_21e05c6.css") : o ? (a = "/passApi/js/uni_loginv4_cf6db29.js", e = "/passApi/js/uni_loginv4_tangram_ce65df7.js", t = "/passApi/css/uni_loginv4_d8ce556.css") : (a = "/passApi/js/uni_login_b2fe708.js", e = "/passApi/js/uni_login_tangram_912687c.js", t = "/passApi/css/uni_login_new_c7a854a.css");
    var r = {
            uni_login: a,
            uni_login_tangram: e,
            uni_loginPad: "/passApi/js/uni_loginPad_8a9f821.js",
            uni_loginPad_tangram: "/passApi/js/uni_loginPad_tangram_d01ddb0.js",
            uni_smsloginEn: "/passApi/js/uni_smsloginEn_776730b.js",
            uni_smsloginEn_tangram: "/passApi/js/uni_smsloginEn_tangram_2b35ed6.js",
            uni_loginWap: "/passApi/js/uni_loginWap_376150f.js",
            uni_loginWap_tangram: "/passApi/js/uni_loginWap_376150f.js",
            uni_accConnect: "/passApi/js/uni_accConnect_e25cbcc.js",
            uni_accConnect_tangram: "/passApi/js/uni_accConnect_tangram_1685327.js",
            uni_accRealName: "/passApi/js/uni_accRealName_57188df.js",
            uni_accRealName_tangram: "/passApi/js/uni_accRealName_tangram_627ae89.js",
            uni_checkPhone: "/passApi/js/uni_checkPhone_d924329.js",
            uni_checkPhone_tangram: "/passApi/js/uni_checkPhone_tangram_a442c7c.js",
            uni_checkIDcard: "/passApi/js/uni_checkIDcard_ac69377.js",
            uni_checkIDcard_tangram: "/passApi/js/uni_checkIDcard_tangram_3b347c7.js",
            uni_accSetPwd: "/passApi/js/uni_accSetPwd_6e851d9.js",
            uni_accSetPwd_tangram: "/passApi/js/uni_accSetPwd_tangram_70ad498.js",
            uni_IDCertify: "/passApi/js/uni_IDCertify_0eafb83.js",
            uni_IDCertify_tangram: "/passApi/js/uni_IDCertify_tangram_6a0bd83.js",
            uni_travelComplete: "/passApi/js/uni_travelComplete_5f4af98.js",
            uni_travelComplete_tangram: "/passApi/js/uni_travelComplete_tangram_b95e8f6.js",
            uni_bindGuide: "/passApi/js/uni_bindGuide_3671a8c.js",
            uni_bindGuide_tangram: "/passApi/js/uni_bindGuide_tangram_279c870.js",
            uni_fillUserName: "/passApi/js/uni_fillUserName_38a073d.js",
            uni_fillUserName_tangram: "/passApi/js/uni_fillUserName_tangram_6912113.js",
            uni_IDCertifyQrcode: "/passApi/js/uni_IDCertifyQrcode_3a0339a.js",
            uni_IDCertifyQrcode_tangram: "/passApi/js/uni_IDCertifyQrcode_tangram_0f7c176.js",
            uni_loadingApi: "/passApi/js/uni_loadingApi_eb97345.js",
            uni_loadingApi_tangram: "/passApi/js/uni_loadingApi_tangram_6f236c6.js",
            uni_secondCardList: "/passApi/js/uni_secondCardList_62d38c0.js",
            uni_secondCardList_tangram: "/passApi/js/uni_secondCardList_tangram_94f42d3.js",
            uni_secondCardVerify: "/passApi/js/uni_secondCardVerify_c4167a0.js",
            uni_secondCardVerify_tangram: "/passApi/js/uni_secondCardVerify_tangram_5ad15c3.js",
            uni_multiBind: "/passApi/js/uni_multiBind_e563850.js",
            uni_multiBind_tangram: "/passApi/js/uni_multiBind_tangram_94ae5db.js",
            uni_multiUnbind: "/passApi/js/uni_multiUnbind_a1a0002.js",
            uni_multiUnbind_tangram: "/passApi/js/uni_multiUnbind_tangram_31a23f5.js",
            uni_changeUser: "/passApi/js/uni_changeUser_cb0e8b1.js",
            uni_changeUser_tangram: "/passApi/js/uni_changeUser_tangram_f55998f.js",
            uni_loginMultichoice: "/passApi/js/uni_loginMultichoice_685d0c3.js",
            uni_loginMultichoice_tangram: "/passApi/js/uni_loginMultichoice_tangram_c74a96b.js",
            uni_confirmWidget: "/passApi/js/uni_confirmWidget_32c10db.js",
            uni_confirmWidget_tangram: "/passApi/js/uni_confirmWidget_tangram_a8882ea.js"
        },
        u = {
            login: t,
            loginWap: "/passApi/css/uni_loginWap_d062be9.css",
            smsloginEn: "/passApi/css/uni_smsloginEn_eef0a6a.css",
            accConnect: "/passApi/css/uni_accConnect_ab6dda9.css",
            accRealName: "/passApi/css/uni_accRealName_a224a37.css",
            secondCardVerify: "/passApi/css/uni_secondCardVerify_1a69328.css",
            secondCardList: "/passApi/css/uni_secondCardList_94f229c.css",
            checkPhone: "/passApi/css/uni_checkPhone_cd7c7a0.css",
            checkIDcard: "/passApi/css/uni_checkIDcard_be79680.css",
            accSetPwd: "/passApi/css/uni_accSetPwd_66adc9b.css",
            IDCertify: "/passApi/css/uni_IDCertify_36e091b.css",
            IDCertifyQrcode: "/passApi/css/uni_IDCertifyQrcode_352899d.css",
            loadingApi: "/passApi/css/uni_loadingApi_f8732c0.css",
            loginPad: "/passApi/css/uni_loginPad_6bad4af.css",
            multiBind: "/passApi/css/uni_multiBind_e8d24e4.css",
            multiUnbind: "/passApi/css/uni_multiUnbind_21428a6.css",
            changeUser: "/passApi/css/uni_changeUser_c7ae7b4.css",
            loginMultichoice: "/passApi/css/uni_loginMultichoice_cb232e6.css",
            confirmWidget: "/passApi/css/uni_confirmWidget_035fb81.css",
            uni_rebindGuide: "/passApi/css/uni_rebindGuide_347ecf2.css",
            travelComplete: "/passApi/css/uni_travelComplete_b06b013.css",
            bindGuide: "/passApi/css/uni_bindGuide_35d4a06.css",
            fillUserName: "/passApi/css/uni_fillUserName_931cb17.css"
        },
        d = i[n] || i["https:"];
    s = s || {}, s.type = s.type || "login";
    var l, m = document,
        g = ("_PassUni" + (new Date).getTime(), d + u[s.type]);
    s.cssUrlWrapper && (g = cssUrlWrapper.join(o ? "uni_loginv4.css" : _ ? "uni_loginv5.css" : "uni_login.css")), l = {
        show: function() {
            return l.loadPass(s.apiOpt), l.willShow = !0, l
        },
        setSubpro: function(i) {
            return s.apiOpt && (s.apiOpt.subpro = i), l
        },
        setMakeText: function(i) {
            return s.apiOpt && (s.apiOpt.makeText = i), l
        },
        loadPass: function() {
            var i = m.createElement("link");
            i.rel = "stylesheet", i.type = "text/css", i.href = g, i.disabled = !1, i.setAttribute("data-for", "result"), m.getElementsByTagName("head")[0].appendChild(i), l.show = function() {
                return l.willShow = !0, l
            }, s.plugCss && (i = m.createElement("link"), i.rel = "stylesheet", i.type = "text/css", i.href = s.plugCss, i.disabled = !1, i.setAttribute("data-for", "result"), m.getElementsByTagName("head")[0].appendChild(i)), l.passCallback(), delete l.loadPass
        },
        passCallback: function() {
            passport.pop.insertScript("https://wappass.baidu.com/static/waplib/moonshad.js?tt=" + (new Date).getTime(), function() {
                l.components.length > 0 ? passport.pop.insertScript(l.components.shift(), l.passCallback) : (passport.pop[s.type](s, l, function() {
                    l.willShow && l.show(), s && s.onRender && s.onRender()
                }), delete l.passCallback, delete l.components)
            })
        },
        components: []
    };
    var j = "uni_" + s.type;
    return s.tangram && (j += "_tangram"), s.apiOpt && s.apiOpt.product + "" == "ik" && Math.random() < .3 && (l.components.push(d + "/passApi/js/uni/passhunt.js"), s.hunter = !0), l.components.push(d + r[j]), s.cache && l.loadPass(s.apiOpt), s.id && m.getElementById(s.id) && (m.getElementById(s.id).onclick = function() {
        l.show()
    }), isSingleInstanceProd(s.apiOpt.product) && isLoginInstance(s.type) && saveInitInstance(l), l
};