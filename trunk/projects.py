#!/usr/bin/python
# -*- coding: utf-8  -*-
listproj = [
    "Afrikaans (af)",
    "Alemannisch (als)",
    "Aragonés (an)",
    "Armâneashti (roa-rup)",
    "Asturianu (ast)",
    "Avañe'ẽ (gn)",
    "Авар (av)",
    "Aymar (ay)",
    "Azərbaycan dili / آذربايجان ديلی (az)",
    "Bahasa Indonesia (id)",
    "Bahasa Melayu (ms)",
    "Bamanankan (bm)",
    "Bân-lâm-gú (zh-min-nan)",
    "Basa Jawa (jv)",
    "Basa Banyumasan (map-bms)",
    "Basa Sunda (su)",
    "Basa Ugi (bug)",
    "Bislama (bi)",
    "Boarisch (bar)",
    "Bosanski (bs)",
    "Brezhoneg (br)",
    "Català (ca)",
    "Chavacano (cbk-zam)",
    "Chamorru (ch)",
    "Čeština (cs)",
    "chiChewa (ny)",
    "chiShona (sn)",
    "chiTumbuka (tum)",
    "chiVenda (ve)",
    "Corsu (co)",
    "Cuengh (za)",
    "Cymraeg (cy)",
    "Dansk (da)",
    "Deitsch (pdc)",
    "Deutsch (de)",
    "Diné bizaad (nv)",
    "dorerin Naoero (na)",
    "Dzhudezmo (lad)",
    "Eesti (et)",
    "Englisc (ang)",
    "English (en)",
    "Español (es)",
    "Esperanto (eo)",
    "Estremeñu (ext)",
    "Euskara (eu)",
    "Faka Tonga (to)",
    "Føroyskt (fo)",
    "Français (fr)",
    "Franco-provençal (frp)",
    "Frysk (fy)",
    "Fulfulde (ff)",
    "Furlan (fur)",
    "Gaeilge (ga)",
    "Gaelg (gv)",
    "Gagana Samoa (sm)",
    "Gàidhlig (gd)",
    "Galego (gl)",
    "Gutisk (got)",
    "Hak-kâ-fa / 客家話 (hak)",
    "Hawaiʻi (haw)",
    "Hornjoserbšćina (hsb)",
    "Hrvatski (hr)",
    "Ido (io)",
    "Ilokano (ilo)",
    "Igbo (ig)",
    "Interlingua (ia)",
    "Interlingue (ie)",
    "Iñupiak (ik)",
    "isiXhosa (xh)",
    "isiZulu (zu)",
    "Íslenska (is)",
    "Italiano (it)",
    "Kajin Majel (mh)",
    "Kalaallisut (kl)",
    "Kapampangan (pam)",
    "Kaszëbsczi (csb)",
    "Kernewek / Karnuack (kw)",
    "Kikongo (kg)",
    "Kikuyu (ki)",
    "Kinyarwandi (rw)",
    "Kırgızca / Кыргызча (ky)",
    "Kirundi (rn)",
    "Kiswahili (sw)",
    "Kreyòl ayisyen (ht)",
    "Kurdî / كوردی (ku)",
    "Ripoarisch (ksh)",
    "Latina (la)",
    "Latviešu (lv)",
    "Lëtzebuergesch (lb)",
    "Lietuvių (lt)",
    "Líguru (lij)",
    "Limburgs (li)",
    "Lingála (ln)",
    "Lojban (jbo)",
    "Luganda (lg)",
    "Lumbaart (lmo)",
    "Magyar (hu)",
    "Malagasy (mg)",
    "Malti (mt)",
    "Māori (mi)",
    "Mìng-dĕ̤ng-ngṳ̄ (cdo)",
    "Myanmasa (my)",
    "Nāhuatl (nah)",
    "Na Vosa Vakaviti (fj)",
    "Nederlands (nl)",
    "Nehiyaw (cr)",
    "Nnapulitano (nap)",
    "Norfuk (pih)",
    "Norsk bokmål (no)",
    "Norsk nynorsk (nn)",
    "Nouormand / Normaund (nrm)",
    "Occitan (oc)",
    "Oromifaa (om)",
    "Oshiwambo (ng)",
    "Pangasinán (pag)",
    "Pāli / पाली (pi)",
    "Papiamentu (pap)",
    "Piemontèis (pms)",
    "Plattdüütsch (nds)",
    "Polski (pl)",
    "Português (pt)",
    "Reo Mā`ohi (ty)",
    "Română (ro)",
    "Romani / रोमानी (rmy)",
    "Rumantsch (rm)",
    "Runa Simi (qu)",
    "Sámegiella (se)",
    "Sängö (sg)",
    "Sardu (sc)",
    "Scots (sco)",
    "seSotho (st)",
    "Setswana (tn)",
    "Shqip (sq)",
    "Sicilianu (scn)",
    "Simple English (simple)",
    "Sinugboanong Binisaya (ceb)",
    "SiSwati (ss)",
    "Slovenčina (sk)",
    "Slovenščina (sl)",
    "Soomaaliga (so)",
    "Srpskohrvatski / Српскохрватски (sh)",
    "Suomi (fi)",
    "Svenska (sv)",
    "Tagalog (tl)",
    "Tatarça (tt)",
    "Tetun (tet)",
    "Tiếng Việt (vi)",
    "Tok Pisin (tpi)",
    "Tsetsêhestâhese (chy)",
    "Türkçe (tr)",
    "Türkmençe / تركمن (tk)",
    "Twi (tw)",
    "Vèneto (vec)",
    "Volapük (vo)",
    "Võro (fiu-vro)",
    "Walon (wa)",
    "West-Vlams (vls)",
    "Winaray (war)",
    "Wollof (wo)",
    "Xitsonga (ts)",
    "Yorùbá (yo)",
    "Žemaitėška (bat-smg)",
    "Ελληνικά (el)",
    "Аҧсуа бызшәа (ab)",
    "Башҡорт (ba)",
    "Беларуская (be)",
    "Български (bg)",
    "Буряад хэлэн (bxr)",
    "Словѣньскъ (cu)",
    "Иронау (os)",
    "Қазақша (kk)",
    "Коми (kv)",
    "Македонски (mk)",
    "Монгол (mn)",
    "Нохчийн (ce)",
    "Русский (ru)",
    "Српски / Srpski (sr)",
    "Тоҷикӣ (tg)",
    "Удмурт (udm)",
    "Українська (uk)",
    "Ўзбек / Oʻzbekche (uz)",
    "Хальмг (xal)",
    "Чӑваш (cv)",
    "Հայերեն (hy)",
    "ქართული (ka)",
    "עברית (he)",
    "ייִדיש (yi)",
    "العربية (ar)",
    "فارسی (fa)",
    "هَوُسَ (ha)",
    "پښتو (ps)",
    "سنڌي (sd)",
    "اردو (ur)",
    "ئۇيغۇرچە / Uyƣurqə (ug)",
    "ܐܪܡܝܐ (arc)",
    "ދިވެހި (dv)",
    "অসমীয়া / Asami (as)",
    "भोजपुरी (bh)",
    "বাংলা (bn)",
    "བོད་ཡིག / Bod skad (bo)",
    "বিষ্ণুপ্রিয়া মণিপুরী (bpy)",
    "ཇོང་ཁ (dz)",
    "ગુજરાતી (gu)",
    "हिन्दी (hi)",
    "ಕನ್ನಡ (kn)",
    "कश्मीरी / كشميري (ks)",
    "മലയാളം (ml)",
    "मराठी (mr)",
    "नेपाली (ne)",
    "नेपाल भाषा (new)",
    "ଓଡ଼ିଆ (or)",
    "ਪਜਾਬੀ / पंजाबी / پنجابي (pa)",
    "संस्कृत (sa)",
    "සිංහල (si)",
    "தமிழ் (ta)",
    "తెలుగు (te)",
    "ភាសាខ្មែរ (km)",
    "ພາສາລາວ (lo)",
    "ไทย (th)",
    "አማርኛ (am)",
    "ትግርኛ (ti)",
    "ᐃᓄᒃᑎᑐᑦ (iu)",
    "ᏣᎳᎩ (chr)",
    "한국어 (ko)",
    "日本語 (ja)",
    "中文 (zh)",
    "吴语 (wuu)",
    "古文 / 文言文 (zh-classical)",
    "粵語 (zh-yue)"]
hashproj = {
    "Afrikaans :(af)":["af.wikipedia","af.wiktionary","af.wikibooks","af.wikiquoute"],
    "Alemannisch :(als)":["als.wikipedia"],
    "Aragonés :(an)":["an.wikipedia","an.wiktionary"],
    "Armâneashti :(roa-rup)":["roa-rup.wikipedia"],
    "Asturianu :(ast)":["ast.wikipedia","ast.wiktionary"],
    "Avañe'ẽ :(gn)":["gn.wikipedia"],
    "Авар :(av)":["av.wikipedia"],
    "Aymar :(ay)":["ay.wikipedia"],
    "Azərbaycan dili / آذربايجان ديلی :(az)":["az.wikipedia"],
    "Bahasa Indonesia :(id)":["id.wikipedia"],
    "Bahasa Melayu :(ms)":["ms.wikipedia","ms.wiktionary"],
    "Bamanankan :(bm)":["bm.wikipedia"],
    "Bân-lâm-gú :(zh-min-nan)":["zh-min-nan.wikipedia","zh-min-nan.wiktionary"],
    "Basa Jawa :(jv)":["jv.wikipedia"],
    "Basa Banyumasan :(map-bms)":["map-bms.wikipedia"],
    "Basa Sunda :(su)":["su.wikipedia"],
    "Basa Ugi :(bug)":["bug.wikipedia"],
    "Bislama :(bi)":["bi.wikipedia"],
    "Boarisch :(bar)":["bar.wikipedia"],
    "Bosanski :(bs)":["bs.wikipedia"],
    "Brezhoneg :(br)":["br.wikipedia"],
    "Català :(ca)":["ca.wikipedia"],
    "Chavacano :(cbk-zam)":["cbk-zam.wikipedia"],
    "Chamorru :(ch)":["ch.wikipedia"],
    "Čeština :(cs)":["cs.wikipedia"],
    "chiChewa :(ny)":["ny.wikipedia"],
    "chiShona :(sn)":["sn.wikipedia"],
    "chiTumbuka :(tum)":["tum.wikipedia"],
    "chiVenda :(ve)":["ve.wikipedia"],
    "Corsu :(co)":["co.wikipedia"],
    "Cuengh :(za)":["za.wikipedia"],
    "Cymraeg :(cy)":["cy.wikipedia"],
    "Dansk :(da)":["da.wikipedia"],
    "Deitsch :(pdc)":["pdc.wikipedia"],
    "Deutsch :(de)":["de.wikipedia"],
    "Diné bizaad :(nv)":["nv.wikipedia"],
    "dorerin Naoero :(na)":["na.wikipedia"],
    "Dzhudezmo :(lad)":["lad.wikipedia"],
    "Eesti :(et)":["et.wikipedia"],
    "Englisc :(ang)":["ang.wikipedia"],
    "English :(en)":["en.wikipedia"],
    "Español :(es)":["es.wikipedia"],
    "Esperanto :(eo)":["eo.wikipedia"],
    "Estremeñu :(ext)":["ext.wikipedia"],
    "Euskara :(eu)":["eu.wikipedia"],
    "Faka Tonga :(to)":["to.wikipedia"],
    "Føroyskt :(fo)":["fo.wikipedia"],
    "Français :(fr)":["fr.wikipedia"],
    "Franco-provençal :(frp)":["frp.wikipedia"],
    "Frysk :(fy)":["fy.wikipedia"],
    "Fulfulde :(ff)":["ff.wikipedia"],
    "Furlan :(fur)":["fur.wikipedia"],
    "Gaeilge :(ga)":["ga.wikipedia"],
    "Gaelg :(gv)":["gv.wikipedia"],
    "Gagana Samoa :(sm)":["sm.wikipedia"],
    "Gàidhlig :(gd)":["gd.wikipedia"],
    "Galego :(gl)":["gl.wikipedia"],
    "Gutisk :(got)":["got.wikipedia"],
    "Hak-kâ-fa / 客家話 :(hak)":["hak.wikipedia"],
    "Hawaiʻi :(haw)":["haw.wikipedia"],
    "Hornjoserbšćina :(hsb)":["hsb.wikipedia"],
    "Hrvatski :(hr)":["hr.wikipedia"],
    "Ido :(io)":["io.wikipedia"],
    "Ilokano :(ilo)":["ilo.wikipedia"],
    "Igbo :(ig)":["ig.wikipedia"],
    "Interlingua :(ia)":["ia.wikipedia"],
    "Interlingue :(ie)":["ie.wikipedia"],
    "Iñupiak :(ik)":["ik.wikipedia"],
    "isiXhosa :(xh)":["xh.wikipedia"],
    "isiZulu :(zu)":["zu.wikipedia"],
    "Íslenska :(is)":["is.wikipedia"],
    "Italiano :(it)":["it.wikipedia"],
    "Kajin Majel :(mh)":["mh.wikipedia"],
    "Kalaallisut :(kl)":["kl.wikipedia"],
    "Kapampangan :(pam)":["pam.wikipedia"],
    "Kaszëbsczi :(csb)":["csb.wikipedia"],
    "Kernewek / Karnuack :(kw)":["kw.wikipedia"],
    "Kikongo :(kg)":["kg.wikipedia"],
    "Kikuyu :(ki)":["ki.wikipedia"],
    "Kinyarwandi :(rw)":["rw.wikipedia"],
    "Kırgızca / Кыргызча :(ky)":["ky.wikipedia"],
    "Kirundi :(rn)":["rn.wikipedia"],
    "Kiswahili :(sw)":["sw.wikipedia"],
    "Kreyòl ayisyen :(ht)":["ht.wikipedia"],
    "Kurdî / كوردی :(ku)":["ku.wikipedia"],
    "Ripoarisch :(ksh)":["ksh.wikipedia"],
    "Latina :(la)":["la.wikipedia"],
    "Latviešu :(lv)":["lv.wikipedia"],
    "Lëtzebuergesch :(lb)":["lb.wikipedia"],
    "Lietuvių :(lt)":["lt.wikipedia"],
    "Líguru :(lij)":["lij.wikipedia"],
    "Limburgs :(li)":["li.wikipedia"],
    "Lingála :(ln)":["ln.wikipedia"],
    "Lojban :(jbo)":["jbo.wikipedia"],
    "Luganda :(lg)":["lg.wikipedia"],
    "Lumbaart :(lmo)":["lmo.wikipedia"],
    "Magyar :(hu)":["hu.wikipedia"],
    "Malagasy :(mg)":["mg.wikipedia"],
    "Malti :(mt)":["mt.wikipedia"],
    "Māori :(mi)":["mi.wikipedia"],
    "Mìng-dĕ̤ng-ngṳ̄ :(cdo)":["cdo.wikipedia"],
    "Myanmasa :(my)":["my.wikipedia"],
    "Nāhuatl :(nah)":["nah.wikipedia"],
    "Na Vosa Vakaviti :(fj)":["fj.wikipedia"],
    "Nederlands :(nl)":["nl.wikipedia"],
    "Nehiyaw :(cr)":["cr.wikipedia"],
    "Nnapulitano :(nap)":["nap.wikipedia"],
    "Norfuk :(pih)":["pih.wikipedia"],
    "Norsk bokmål :(no)":["no.wikipedia"],
    "Norsk nynorsk :(nn)":["nn.wikipedia"],
    "Nouormand / Normaund :(nrm)":["nrm.wikipedia"],
    "Occitan :(oc)":["oc.wikipedia"],
    "Oromifaa :(om)":["om.wikipedia"],
    "Oshiwambo :(ng)":["ng.wikipedia"],
    "Pangasinán :(pag)":["pag.wikipedia"],
    "Pāli / पाली :(pi)":["pi.wikipedia"],
    "Papiamentu :(pap)":["pap.wikipedia"],
    "Piemontèis :(pms)":["pms.wikipedia"],
    "Plattdüütsch :(nds)":["nds.wikipedia"],
    "Polski :(pl)":["pl.wikipedia"],
    "Português :(pt)":["pt.wikipedia"],
    "Reo Mā`ohi :(ty)":["ty.wikipedia"],
    "Română :(ro)":["ro.wikipedia"],
    "Romani / रोमानी :(rmy)":["rmy.wikipedia"],
    "Rumantsch :(rm)":["rm.wikipedia"],
    "Runa Simi :(qu)":["qu.wikipedia"],
    "Sámegiella :(se)":["se.wikipedia"],
    "Sängö :(sg)":["sg.wikipedia"],
    "Sardu :(sc)":["sc.wikipedia"],
    "Scots :(sco)":["sco.wikipedia"],
    "seSotho :(st)":["st.wikipedia"],
    "Setswana :(tn)":["tn.wikipedia"],
    "Shqip :(sq)":["sq.wikipedia"],
    "Sicilianu :(scn)":["scn.wikipedia"],
    "Simple English :(simple)":["simple.wikipedia"],
    "Sinugboanong Binisaya :(ceb)":["ceb.wikipedia"],
    "SiSwati :(ss)":["ss.wikipedia"],
    "Slovenčina :(sk)":["sk.wikipedia"],
    "Slovenščina :(sl)":["sl.wikipedia"],
    "Soomaaliga :(so)":["so.wikipedia"],
    "Srpskohrvatski / Српскохрватски :(sh)":["sh.wikipedia"],
    "Suomi :(fi)":["fi.wikipedia"],
    "Svenska :(sv)":["sv.wikipedia"],
    "Tagalog :(tl)":["tl.wikipedia"],
    "Tatarça :(tt)":["tt.wikipedia"],
    "Tetun :(tet)":["tet.wikipedia"],
    "Tiếng Việt :(vi)":["vi.wikipedia"],
    "Tok Pisin :(tpi)":["tpi.wikipedia"],
    "Tsetsêhestâhese :(chy)":["chy.wikipedia"],
    "Türkçe :(tr)":["tr.wikipedia"],
    "Türkmençe / تركمن :(tk)":["tk.wikipedia"],
    "Twi :(tw)":["tw.wikipedia"],
    "Vèneto :(vec)":["vec.wikipedia"],
    "Volapük :(vo)":["vo.wikipedia"],
    "Võro :(fiu-vro)":["fiu-vro.wikipedia"],
    "Walon :(wa)":["wa.wikipedia"],
    "West-Vlams :(vls)":["vls.wikipedia"],
    "Winaray :(war)":["war.wikipedia"],
    "Wollof :(wo)":["wo.wikipedia"],
    "Xitsonga :(ts)":["ts.wikipedia"],
    "Yorùbá :(yo)":["yo.wikipedia"],
    "Žemaitėška :(bat-smg)":["bat-smg.wikipedia"],
    "Ελληνικά :(el)":["el.wikipedia"],
    "Аҧсуа бызшәа :(ab)":["ab.wikipedia"],
    "Башҡорт :(ba)":["ba.wikipedia"],
    "Беларуская :(be)":["be.wikipedia"],
    "Български :(bg)":["bg.wikipedia"],
    "Буряад хэлэн :(bxr)":["bxr.wikipedia"],
    "Словѣньскъ :(cu)":["cu.wikipedia"],
    "Иронау :(os)":["os.wikipedia"],
    "Қазақша :(kk)":["kk.wikipedia"],
    "Коми :(kv)":["kv.wikipedia"],
    "Македонски :(mk)":["mk.wikipedia"],
    "Монгол :(mn)":["mn.wikipedia"],
    "Нохчийн :(ce)":["ce.wikipedia"],
    "Русский :(ru)":["ru.wikipedia"],
    "Српски / Srpski :(sr)":["sr.wikipedia"],
    "Тоҷикӣ :(tg)":["tg.wikipedia"],
    "Удмурт :(udm)":["udm.wikipedia"],
    "Українська :(uk)":["uk.wikipedia"],
    "Ўзбек / Oʻzbekche :(uz)":["uz.wikipedia"],
    "Хальмг :(xal)":["xal.wikipedia"],
    "Чӑваш :(cv)":["cv.wikipedia"],
    "Հայերեն :(hy)":["hy.wikipedia"],
    "ქართული :(ka)":["ka.wikipedia"],
    "עברית :(he)":["he.wikipedia"],
    "ייִדיש :(yi)":["yi.wikipedia"],
    "العربية :(ar)":["ar.wikipedia"],
    "فارسی :(fa)":["fa.wikipedia"],
    "هَوُسَ :(ha)":["ha.wikipedia"],
    "پښتو :(ps)":["ps.wikipedia"],
    "سنڌي :(sd)":["sd.wikipedia"],
    "اردو :(ur)":["ur.wikipedia"],
    "ئۇيغۇرچە / Uyƣurqə :(ug)":["ug.wikipedia"],
    "ܐܪܡܝܐ :(arc)":["arc.wikipedia"],
    "ދިވެހި :(dv)":["dv.wikipedia"],
    "অসমীয়া / Asami :(as)":["as.wikipedia"],
    "भोजपुरी :(bh)":["bh.wikipedia"],
    "বাংলা :(bn)":["bn.wikipedia"],
    "བོད་ཡིག / Bod skad :(bo)":["bo.wikipedia"],
    "বিষ্ণুপ্রিয়া মণিপুরী :(bpy)":["bpy.wikipedia"],
    "ཇོང་ཁ :(dz)":["dz.wikipedia"],
    "ગુજરાતી :(gu)":["gu.wikipedia"],
    "हिन्दी :(hi)":["hi.wikipedia"],
    "ಕನ್ನಡ :(kn)":["kn.wikipedia"],
    "कश्मीरी / كشميري :(ks)":["ks.wikipedia"],
    "മലയാളം :(ml)":["ml.wikipedia"],
    "मराठी :(mr)":["mr.wikipedia"],
    "नेपाली :(ne)":["ne.wikipedia"],
    "नेपाल भाषा :(new)":["new.wikipedia"],
    "ଓଡ଼ିଆ :(or)":["or.wikipedia"],
    "ਪਜਾਬੀ / पंजाबी / پنجابي :(pa)":["pa.wikipedia"],
    "संस्कृत :(sa)":["sa.wikipedia"],
    "සිංහල :(si)":["si.wikipedia"],
    "தமிழ் :(ta)":["ta.wikipedia"],
    "తెలుగు :(te)":["te.wikipedia"],
    "ភាសាខ្មែរ :(km)":["km.wikipedia"],
    "ພາສາລາວ :(lo)":["lo.wikipedia"],
    "ไทย :(th)":["th.wikipedia"],
    "አማርኛ :(am)":["am.wikipedia"],
    "ትግርኛ :(ti)":["ti.wikipedia"],
    "ᐃᓄᒃᑎᑐᑦ :(iu)":["iu.wikipedia"],
    "ᏣᎳᎩ :(chr)":["chr.wikipedia"],
    "한국어 :(ko)":["ko.wikipedia"],
    "日本語 :(ja)":["ja.wikipedia"],
    "中文 :(zh)":["zh.wikipedia"],
    "吴语 :(wuu)":["wuu.wikipedia"],
    "古文 / 文言文 :(zh-classical)":["zh-classical.wikipedia"],
    "粵語 (zh-yue)":""}
