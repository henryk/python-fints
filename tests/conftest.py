import pytest

COMPLICATED_EXAMPLE = \
(b'HNHBK:1:3+000000021319+300+430711670077=043999659571CN9D=+1+430711670077=043'
 b"999659571CN9D=:1'HNVSK:998:3+PIN:1+998+1+2::0+1:20180730:135639+2:2:13:@8@00"
 b"000000:5:1+280:15050500:hermes:S:0:0+0'HNVSD:999:1+@21094@HNSHK:2:4+PIN:1+99"
 b'9+1259150+1+1+2::0+1+1:20180730:135639+1:999:1+6:10:16+280:15050500:hermes:S'
 b":0:0'HIRMG:3:2+3060::Bitte beachten Sie die enthaltenen Warnungen/Hinweise.'"
 b"HIRMS:4:2:5+0020::Auftrag ausgef\xfchrt.'HIRMS:5:2:4+3050::UPD nicht mehr a"
 b'ktuell, aktuelle Version enthalten.+3050::BPD nicht mehr aktuell, aktuelle V'
 b'ersion enthalten.+3920::Zugelassene Zwei-Schritt-Verfahren f\xfcr den Benut'
 b"zer.:910:911:912+0020::Der Auftrag wurde ausgef\xfchrt.'HIBPA:6:3:4+3+280:1"
 b"5050500+Sparkasse Vorpommern+3+1+300'HIKOM:7:4:4+280:15050500+1+3:banking-mv"
 b"6.s-fints-pt-mv.de/fints30+2:banking-mv6.s-fints-pt-mv.de::MIM:1'HISHV:8:3:4"
 b"+N+RAH:7+PIN:1+DDV:1'HICERS:9:1:4+999+0+4+1:N:J:J:N:RAH:7'HICSUS:10:1:4+1+1+"
 b'1+INTC;CORT:urn?:iso?:std?:iso?:20022?:tech?:xsd?:pain.001.003.03:urn?:iso?:'
 b"std?:iso?:20022?:tech?:xsd?:pain.001.001.03'DIWOKS:11:1:4+1+1+1+9999999,99:E"
 b"UR'DIWDHS:12:1:4+1+1+1+J:N:730'DIBVES:13:1:4+1+1+1+E'DIPTZS:14:1:4+1+1+1+J'D"
 b"IEEAS:15:1:4+1+1+1+DKPTZ:1:N'DIALES:16:1:4+1+1+1+V-EC-KARTE:V-S-CARD:V-WERTK"
 b"ARTE'DIALLS:17:1:4+1+1+1'DIALNS:18:1:4+1+1+1+V-EC-KARTE:V-S-CARD:V-WERTKARTE"
 b"'DIANAS:19:1:4+1+1+1+1:15'DIANLS:20:1:4+1+1+1'DIBAZS:21:2:4+1+1+1+J:J'DIBKDS"
 b":22:4:4+1+1+1'DIBKUS:23:3:4+1+1+1+J:N'DIBUMS:24:3:4+1+1+1+N'DIBVAS:25:1:4+1+"
 b"1+1'DIBVBS:26:1:4+1+1+1'DIBVDS:27:1:4+1+1+1'DIBVKS:28:1:4+1+1+1+J:V-EC-KARTE"
 b":V-S-CARD:V-WERTKARTE'DIBVPS:29:1:4+1+1+1+8:20'DIBVRS:30:1:4+1+1+1+8:20::N:N"
 b"'DIBVSS:31:1:4+1+1+1'DIBVSS:32:2:4+1+1+1'DIDFAS:33:1:4+1+1+1+N'DIDFBS:34:1:4"
 b"+1+1+1'DIDFCS:35:1:4+1+1+1'DIDFDS:36:1:4+1+1+1'DIDFLS:37:1:4+1+1+1'DIDFUS:38"
 b":1:4+1+1+1+N'DIDFUS:39:2:4+1+1+1+N'DIDIHS:40:1:4+1+1+1'DIDFSS:41:2:4+1+1+1+N"
 b':1;DekaBank-Konzern;5;Swisscanto;7;JPMorgan Fleming;8;Lombard Odier;10;Frank'
 b'lin Templeton;11;Gartmore;12;Goldman Sachs;13;Black Rock Merrill;14;Threadne'
 b'edle;15;UBS;16;Schroders:10_10:Aktienfonds Asien - Pazifik ohne Japan:10_20:'
 b'Aktienfonds Branche:10_30:Aktienfonds Deutschland:10_40:Aktienfonds Emerging'
 b' Markets:10_50:Aktienfonds Euroland:10_60:Aktienfonds Europa L\xe4nder:10_7'
 b'0:Aktienfonds Europa:10_80:Aktienfonds Japan:10_90:Aktienfonds Lateinamerika'
 b':10_100:Aktienfonds Nordamerika:10_110:Aktienfonds Osteuropa:10_120:Aktienfo'
 b'nds Welt:10_400:Aktienfonds Afrika:10_410:Aktienfonds Mittlerer Osten:10_420'
 b':Aktienfonds Nordeuropa:20_130:Dachfonds Chance Plus:20_140:Dachfonds Chance'
 b':20_150:Dachfonds Ertrag Plus:20_160:Dachfonds Ertrag:20_170:Dachfonds Wachs'
 b'tum:20_180:Dachfonds laufzeitbegrenzt:30_430:Garantiefonds:40_200:Geldmarktf'
 b'onds:40_210:Geldmarktnahe Fonds:50_220:Alternative Investmentfonds Hedgefond'
 b's:50_230:Alternative Investmentfonds Private Equity:50_240:Alternative Inves'
 b'tmentfonds Rohstofffonds:60_250:Sonderkonzepte Absolute-/Total-Returnstrateg'
 b'iefonds:60_260:Sonderkonzepte Altersvorsorgefonds:60_270:Sonderkonzepte Inst'
 b'itutionelle Fondskonzepte:60_280:Sonderkonzepte Steuerorientierte Fonds:70_3'
 b'0:Immobilienfonds Deutschland:70_70:Immobilienfonds Europa:70_120:Immobilien'
 b'fonds Welt:80_50:Mischfonds Euroland:80_290:Mischfonds ausgewogen:80_300:Mis'
 b'chfonds dynamisch:80_310:Mischfonds flexibel:80_320:Mischfonds konservativ:9'
 b'0_330:Rentenfonds Inflationsindexierte Anleihen:90_340:Rentenfonds Laufzeitf'
 b'onds:90_350:Rentenfonds MBS:90_360:Rentenfonds Nachranganleihen:90_370:Rente'
 b'nfonds Staatsanleihen:90_380:Rentenfonds Unternehmensanleihen:90_390:Rentenf'
 b"onds Wandelanleihen'DIDDIS:42:1:4+1+1+1+DKDOF;2:DKDFO;2'DIDFOS:43:2:4+1+1+1'"
 b"DIDFPS:44:2:4+1+1+1'DIDPFS:45:2:4+1+1+1'DIDFES:46:2:4+1+1+1'DIDEFS:47:2:4+1+"
 b"1+1'DIDOFS:48:2:4+1+1+1'DIFAFS:49:2:4+1+1+1+N:N'DIGBAS:50:1:4+1+1+1'DIGBSS:5"
 b"1:1:4+1+1+1+J'DIKAUS:52:3:4+1+1+1+N'DIKKAS:53:2:4+1+1+1+N:N:2'DIKKSS:54:3:4+"
 b"1+1+1'DIKKUS:55:2:4+1+1+1+90:N:J'DIKSBS:56:1:4+3+1+1+J'DIKSPS:57:1:4+3+1+1+;"
 b':sepade.pain.001.001.02.xsd:sepade.pain.001.002.02.xsd:sepade.pain.001.002.0'
 b'3.xsd:urn?:iso?:std?:iso?:20022?:tech?:xsd?:pain.001.003.03:urn?:iso?:std?:i'
 b"so?:20022?:tech?:xsd?:pain.001.001.03'DIPAES:58:1:4+1+1'DIPSAS:59:1:4+1+1'DI"
 b"PSPS:60:1:4+1+1'DIQUOS:61:1:4+1+1+1'DIQUTS:62:1:4+1+1+1'DITLAS:63:1:4+1+1'DI"
 b"TLFS:64:1:4+1+1+N'DITLFS:65:2:4+1+1+N'DITSPS:66:1:4+1+1+N'DIVVDS:67:1:4+3+1+"
 b"1'DIVVUS:68:1:4+3+1+1+N:J'DIWAPS:69:1:4+1+1+J:STOP;SLOS;LMTO;MAKT:J:J:GDAY;G"
 b"TMO;GTHD:J:1:N:N:N:9999999,99:EUR'DIWAPS:70:4:4+1+1+1+J:STOP;STLI;LMTO;MAKT;"
 b"OCOO;TRST:J:J:J:J:J:GDAY;GTMO;GTHD:J:1:N:N:N:9999999,99:EUR'DIWDGS:71:1:4+1+"
 b"1+1+J:N:N'DIWGVS:72:1:4+1+1+1+J:730:N'DIWLVS:73:1:4+1+1+1+J:365:N'DINZPS:74:"
 b"3:4+1+1+1+N:N:4:N:N:::N:J'DIFOPS:75:3:4+1+1+1+N:4:N:N:N::::MAKT:N:J'DIFPOS:7"
 b"6:3:4+1+1+1+N:4:N:N:::N:J'DIWOPS:77:5:4+1+1+1+0:N:4:N:N::::9999999,99:EUR:ST"
 b'OP;STLI;LMTO;MAKT;OCOO;TRST:BUYI;SELL;AUCT;CONT;ALNO;DIHA:GDAY;GTMO;GTHD;GTC'
 b"A;IOCA;OPEN;CLOS;FIKI:N:J'DIWVBS:78:1:4+1+1+1+N:N'DIZDFS:79:2:4+1+1+1'DIZDLS"
 b":80:2:4+1+1+1'HIAUBS:81:5:4+1+1+1'HIBMES:82:1:4+1+1+1+2:28:2:28:1000:J:N'HIB"
 b"SES:83:1:4+1+1+1+2:28:2:28'HICAZS:84:1:4+3+1+1+450:N:N:urn?:iso?:std?:iso?:2"
 b"0022?:tech?:xsd?:camt.052.001.02'HICCMS:85:1:4+1+1+1+1000:J:N'HICCSS:86:1:4+"
 b"1+1+1'HICDBS:87:1:4+3+1+1+N'HICDES:88:1:4+3+1+1+4:0:9999:0102030612:01020304"
 b"050607080910111213141516171819202122232425262728293099'HICDLS:89:1:4+3+1+1+0"
 b":9999:J:J'HICDNS:90:1:4+3+1+1+0:0:9999:J:J:J:J:J:N:J:J:J:0102030612:01020304"
 b"050607080910111213141516171819202122232425262728293099'HICDUS:91:1:4+3+1+1+1"
 b":0:9999:1:N:N'HICMBS:92:1:4+1+1+1+N:J'HICMES:93:1:4+1+1+1+1:360:1000:J:N'HIC"
 b"MLS:94:1:4+1+1+1'HICSAS:95:1:4+1+1+1+1:360'HICSBS:96:1:4+1+1+1+N:J'HICSES:97"
 b":1:4+1+1+1+1:360'HICSLS:98:1:4+1+1+1+J'HICUBS:99:1:4+3+1+1+J'HICUMS:100:1:4+"
 b'3+1+1+;:sepade.pain.001.001.02.xsd:sepade.pain.001.002.02.xsd:sepade.pain.00'
 b'1.002.03.xsd:urn?:iso?:std?:iso?:20022?:tech?:xsd?:pain.001.003.03:urn?:iso?'
 b":std?:iso?:20022?:tech?:xsd?:pain.001.001.03'HIDMCS:101:1:4+1+1+1+1000:J:N:2"
 b":28:2:28::urn?:iso?:std?:iso?:20022?:tech?:xsd?:pain.008.003.02'HIDMES:102:1"
 b":4+1+1+1+2:28:2:28:1000:J:N'HIDSBS:103:1:4+3+1+1+J:J:56'HIDSCS:104:1:4+1+1+1"
 b"+2:28:2:28::urn?:iso?:std?:iso?:20022?:tech?:xsd?:pain.008.003.02'HIDSES:105"
 b":1:4+1+1+1+2:28:2:28'HIDSWS:106:1:4+1+1+1+N'HIEKAS:107:2:4+1+1+1+J:J:N:1'HIE"
 b"KAS:108:3:4+1+1+1+J:J:N:1'HIEKPS:109:1:4+1+1+1+J:J:N'HIFGBS:110:2:4+3+1'HIFG"
 b"BS:111:3:4+3+1'HIFRDS:112:1:4+1+1'HIFRDS:113:4:4+1+1+1+N:J:N:0:Kreditinstitu"
 b"t:1:DekaBank'HIKAZS:114:4:4+3+1+360:J'HIKAZS:115:5:4+3+1+360:J:N'HIKDMS:116:"
 b"2:4+3+0+2048'HIKDMS:117:3:4+3+0+2048'HIKDMS:118:4:4+3+0+2048'HIKIFS:119:1:4+"
 b"1+1'HIKIFS:120:4:4+1+1+1+J:J'HIKIFS:121:5:4+1+1+1+J:J'HIKIFS:122:6:4+1+1+1+J"
 b":J'HIMTAS:123:1:4+1+1+1+N'HIMTAS:124:2:4+1+1+1+N:J'HIMTFS:125:1:4+1+1+1'HIMT"
 b"RS:126:1:4+1+1+1+N'HIMTRS:127:2:4+1+1+1+N:J'HINEAS:128:1:4+1+1+1:2:3:4'HINEZ"
 b"S:129:3:4+1+1+1+N:N:4:N:N:::N:J'HIWFOS:130:3:4+1+1+1+N:4:N:N:N::::MAKT:N:J'H"
 b'IWPOS:131:5:4+1+1+1+0:N:4:N:N::::9999999,99:EUR:STOP;STLI;LMTO;MAKT;OCOO;TRS'
 b"T:BUYI;SELL;AUCT;CONT;ALNO;DIHA:GDAY;GTMO;GTHD;GTCA;IOCA;OPEN;CLOS;FIKI:N:J'"
 b'HIWSDS:132:5:4+3+1+1+J:A;Inland DAX:B;Inland Sonstige:C;Ausland Europa:D;Aus'
 b"land Sonstige'HIFPOS:133:3:4+1+1+1+N:4:N:N:::N:J'HIPAES:134:1:4+1+1+1'HIPPDS"
 b':135:1:4+1+1+1+1:Telekom:Xtra-Card:N:::15;30;50:2:Vodafone:CallYa:N:::15;25;'
 b'50:3:E-Plus:Free and easy:N:::15;20;30:4:O2:Loop:N:::15;20;30:5:congstar:con'
 b'gstar:N:::15;30;50:6:blau:blau:N:::15;20;30:8:o.tel.o:o.tel.o:N:::9;19;29:9:'
 b"SIM Guthaben:SIM Guthaben:N:::15;30;50'HIQTGS:136:1:4+1+1+1'HISALS:137:3:4+3"
 b"+1'HISALS:138:4:4+3+1'HISALS:139:5:4+3+1'HISPAS:140:1:4+1+1+1+J:N:N:sepade.p"
 b'ain.001.001.02.xsd:sepade.pain.001.002.02.xsd:sepade.pain.001.002.03.xsd:sep'
 b'ade.pain.008.002.02.xsd:urn?:iso?:std?:iso?:20022?:tech?:xsd?:pain.001.003.0'
 b'3:urn?:iso?:std?:iso?:20022?:tech?:xsd?:pain.008.003.02:urn?:iso?:std?:iso?:'
 b'20022?:tech?:xsd?:pain.001.001.03:urn?:iso?:std?:iso?:20022?:tech?:xsd?:pain'
 b".008.001.02'HISPAS:141:2:4+1+1+1+J:N:N:N:sepade.pain.001.001.02.xsd:sepade.p"
 b'ain.001.002.02.xsd:sepade.pain.001.002.03.xsd:sepade.pain.008.002.02.xsd:urn'
 b'?:iso?:std?:iso?:20022?:tech?:xsd?:pain.001.003.03:urn?:iso?:std?:iso?:20022'
 b'?:tech?:xsd?:pain.008.003.02:urn?:iso?:std?:iso?:20022?:tech?:xsd?:pain.001.'
 b"001.03:urn?:iso?:std?:iso?:20022?:tech?:xsd?:pain.008.001.02'HITABS:142:2:4+"
 b"1+1+1'HITABS:143:3:4+1+1+1'HITABS:144:4:4+1+1+1'HITAUS:145:1:4+1+1+1+N:N:J'H"
 b"ITAZS:146:1:4+1+1+1'HITAZS:147:2:4+1+1+1'HITMLS:148:1:4+1+1+1'HITSYS:149:1:4"
 b"+1+1+1+N:N'HIWDUS:150:4:4+3+1+999'HIWFPS:151:2:4+3+1+RENTEN:INVESTMENTFONDS:"
 b'GENUSSSCHEINE:SPARBRIEFE:UNTERNEHMENSANLEIHEN:EMERGING MARKET ANLEIHEN:STRUK'
 b'TURIERTE ANLEIHEN:ZERTIFIKATE:AKTIEN:OPTIONSSCHEINE:ALLE ANGEBOTE EIGENES IN'
 b"STITUT:ALLE ANGEBOTE UEBERGEORD. INSTITUTE'HIWOAS:152:2:4+1+1+J:STOP;SLOS;LM"
 b"TO;MAKT:J:J:GDAY;GTMO;GTHD:J:1:N:N:N:9999999,99:EUR'HIWOAS:153:4:4+1+1+1+J:S"
 b'TOP;STLI;LMTO;MAKT;OCOO;TRST:J:J:J:J:J:GDAY;GTMO;GTHD:J:1:N:N:N:9999999,99:E'
 b"UR'HIWPDS:154:3:4+3+1+J'HIWPDS:155:5:4+1+1+J:N:N'HIWPRS:156:1:4+3+1+J:J:N:N:"
 b':Aktien:Festverzinsliche Wertpapiere:Fonds:Fremdw\xe4hrungsanleihen:Genusss'
 b"cheine:Indexzertifikate:Optionsscheine:Wandel- und Optionsanleihen cum'HIWPS"
 b"S:157:1:4+3+1+J'HIWSOS:158:4:4+3+1+1+J:J:90:1:2:3:4:5:6:7:8:9:10:11'HIWSOS:1"
 b"59:5:4+3+1+1+J:J:90:1:2:3:4:5:6:7:8:9:10:11:12:13:14:15:16:17'HITANS:160:1:4"
 b'+1+1+1+J:N:0:0:920:2:smsTAN:smsTAN:6:1:TAN-Nummer:3:1:J:J:900:2:iTAN:iTAN:6:'
 b"1:TAN-Nummer:3:1:J:J'HITANS:161:3:4+1+1+1+J:N:0:910:2:HHD1.3.0:chipTAN manue"
 b'll:6:1:TAN-Nummer:3:1:J:2:0:N:N:N:00:0:1:911:2:HHD1.3.0OPT:chipTAN optisch:6'
 b':1:TAN-Nummer:3:1:J:2:0:N:N:N:00:0:1:912:2:HHD1.3.0USB:chipTAN USB:6:1:TAN-N'
 b'ummer:3:1:J:2:0:N:N:N:00:0:1:920:2:smsTAN:smsTAN:6:1:TAN-Nummer:3:1:J:2:0:N:'
 b'N:N:00:2:5:921:2:pushTAN:pushTAN:6:1:TAN-Nummer:3:1:J:2:0:N:N:N:00:2:2:900:2'
 b":iTAN:iTAN:6:1:TAN-Nummer:3:1:J:2:0:N:N:N:00:0:0'HIPINS:162:1:4+1+1+0+5:5:6:"
 b'USERID:CUSTID:HKAUB:J:HKBME:J:HKBSE:J:HKCAZ:N:HKCCM:J:HKCCS:J:HKCDB:N:HKCDE:'
 b'J:HKCDL:J:HKCDN:J:HKCDU:J:HKCMB:N:HKCME:J:HKCML:J:HKCSA:J:HKCSB:N:HKCSE:J:HK'
 b'CSL:J:HKCSU:J:HKCUB:N:HKCUM:J:HKDMC:J:HKDME:J:HKDSB:N:HKDSC:J:HKDSE:J:HKDSW:'
 b'J:HKEKA:N:HKEKP:N:HKFGB:N:HKFRD:N:HKKAZ:N:HKKDM:J:HKKIF:N:HKMTA:J:HKMTF:N:HK'
 b'MTR:J:HKNEA:N:HKNEZ:J:HKWFO:J:HKWPO:J:HKFPO:J:HKWSD:N:HKPAE:J:HKPPD:J:HKQTG:'
 b'N:HKSAL:N:HKSPA:N:HKTAB:N:HKTAU:N:HKTAZ:N:HKTML:N:HKTSY:N:HKUTA:N:HKWDU:N:HK'
 b'WFP:N:HKWOA:J:HKWPD:N:HKWPK:N:HKWPR:N:HKWPS:J:HKWSO:N:HKTAN:N:DKBKD:N:DKBKU:'
 b'N:DKBUM:N:DKFDA:N:DKPAE:N:DKPSA:J:DKPSP:N:DKTLA:N:DKTLF:J:DKTSP:N:DKWAP:N:DK'
 b'ALE:J:DKALL:J:DKALN:J:DKANA:J:DKANL:J:DKBAZ:N:DKBVA:J:DKBVB:J:DKBVD:N:DKBVK:'
 b'N:DKBVP:J:DKBVR:J:DKBVS:N:DKDFA:N:DKDFB:N:DKDFC:J:DKDFD:N:DKDFL:J:DKDFU:N:DK'
 b'DIH:J:DKDFS:N:DKDDI:N:DKDFO:J:DKDFP:J:DKDPF:N:DKDFE:J:DKDEF:N:DKDOF:N:DKFAF:'
 b'N:DKGBA:J:DKGBS:J:DKKAU:N:DKKKA:N:DKKKS:N:DKKKU:N:DKKSB:N:DKKSP:N:DKQUO:N:DK'
 b'QUT:N:DKVVD:N:DKVVU:N:DKWDG:N:DKWGV:N:DKWLV:N:DKNZP:N:DKFOP:N:DKFPO:N:DKWOP:'
 b"N:DKWVB:N:DKZDF:J:DKZDL:J:DKWOK:N:DKWDH:N:DKBVE:J:DKPTZ:N:DKEEA:N'HIAZSS:163"
 b':1:4+1+1+1+1:N:::::::::::HKFGB;2;0;1;811:DKDFU;1;0;1;811:DKDOF;2;0;1;811:DKD'
 b'FB;1;0;1;811:HKCSU;1;0;1;811:HKTAB;4;0;1;811:DKDIH;1;0;1;811:DKVVD;1;0;1;811'
 b':HKCDB;1;0;1;811:HKWPS;1;0;1;811:DKDFP;2;0;1;811:DKTLA;1;0;1;811:DKBVP;1;0;1'
 b';811:DKKSB;1;0;1;811:HKDME;1;0;1;811:HKWPD;3;0;1;811:DKEEA;1;0;1;811:DKFAF;2'
 b';0;1;811:HKCSL;1;0;1;811:HKCML;1;0;1;811:HKCUM;1;0;1;811:DKDEF;2;0;1;811:HKF'
 b'GB;3;0;1;811:HKCCM;1;0;1;811:DKDFD;1;0;1;811:HKTAU;1;0;1;811:HKWFP;2;0;1;811'
 b':DKWAP;1;0;1;811:DKALE;1;0;1;811:HKCCS;1;0;1;811:DKBVS;1;0;1;811:HKFRD;1;0;1'
 b';811:DKGBA;1;0;1;811:DKZDL;2;0;1;811:HKTAB;2;0;1;811:HKMTA;1;0;1;811:DKBAZ;2'
 b';0;1;811:HKCME;1;0;1;811:HKQTG;1;0;1;811:DKWOK;1;0;1;811:DKALN;1;0;1;811:DKF'
 b'OP;3;0;1;811:DKBVS;2;0;1;811:DKBUM;3;0;1;811:HKWSO;4;0;1;811:HKTAZ;1;0;1;811'
 b':HKPAE;1;0;1;811:DKWGV;1;0;1;811:HKNEZ;3;0;1;811:DKDFU;2;0;1;811:HKDMC;1;0;1'
 b';811:HKAUB;5;0;1;811:DKWDH;1;0;1;811:DKPAE;1;0;1;811:HKTAB;3;0;1;811:HKDSC;1'
 b';0;1;811:DKWVB;1;0;1;811:HKBSE;1;0;1;811:DKWAP;4;0;1;811:DKDFL;1;0;1;811:HKW'
 b'PO;5;0;1;811:HKTAZ;2;0;1;811:DKWOP;5;0;1;811:HKMTR;2;0;1;811:HKDSE;1;0;1;811'
 b':HKTSY;1;0;1;811:DKKSP;1;0;1;811:HKWOA;4;0;1;811:DKTSP;1;0;1;811:HKKIF;1;0;1'
 b';811:HKKDM;4;0;1;811:DKGBS;1;0;1;811:HKWPR;1;0;1;811:HKSPA;1;0;1;811:HKWFO;3'
 b';0;1;811:DKWLV;1;0;1;811:HKKAZ;4;0;1;811:HKKIF;4;0;1;811:HKKAZ;5;0;1;811:HKE'
 b'KP;1;0;1;811:DKTLF;2;0;1;811:DKFPO;3;0;1;811:HKPPD;1;0;1;811:HKMTA;2;0;1;811'
 b':HKCSA;1;0;1;811:DKWDG;1;0;1;811:DKDFE;2;0;1;811:DKQUO;1;0;1;811:HKMTR;1;0;1'
 b';811:DKALL;1;0;1;811:DKPSP;1;0;1;811:HKIDN;2;0;1;811:HKWPD;5;0;1;811:HKCER;1'
 b';0;1;811:DKBKD;4;0;1;811:HKDSW;1;0;1;811:HKCMB;1;0;1;811:DKKKS;3;0;1;811:HKW'
 b'SO;5;0;1;811:HKFPO;3;0;1;811:HKSAL;3;0;1;811:HKCDE;1;0;1;811:DKBVD;1;0;1;811'
 b':HKSPA;2;0;1;811:HKFRD;4;0;1;811:DKTLF;1;0;1;811:DKZDF;2;0;1;811:DKKKU;2;0;1'
 b';811:HKEKA;3;0;1;811:DKPTZ;1;0;1;811:DKBVK;1;0;1;811:DKPSA;1;0;1;811:HKMTF;1'
 b';0;1;811:DKDFA;1;0;1;811:HKWOA;2;0;1;811:DKDDI;1;0;1;811:DKNZP;3;0;1;811:HKC'
 b'DL;1;0;1;811:HKCSE;1;0;1;811:HKSAL;4;0;1;811:HKWDU;4;0;1;811:DKKAU;3;0;1;811'
 b':DKANL;1;0;1;811:HKNEA;1;0;1;811:HKKDM;2;0;1;811:DKVVU;1;0;1;811:HKCDU;1;0;1'
 b';811:HKKIF;6;0;1;811:HKCUB;1;0;1;811:HKTAN;1;0;1;811:DKDFO;2;0;1;811:DKQUT;1'
 b';0;1;811:HKCDN;1;0;1;811:HKEKA;2;0;1;811:DKBVA;1;0;1;811:DKKKA;2;0;1;811:DKD'
 b'PF;2;0;1;811:DKBVR;1;0;1;811:DKBVE;1;0;1;811:DKBVB;1;0;1;811:HKSAL;5;0;1;811'
 b':DKANA;1;0;1;811:HKKDM;3;0;1;811:DKBKU;3;0;1;811:HKWSD;5;0;1;811:HKCAZ;1;0;1'
 b';811:HKCSB;1;0;1;811:HKTML;1;0;1;811:HKKIF;5;0;1;811:DKDFC;1;0;1;811:DKDFS;2'
 b";0;1;811:HKDSB;1;0;1;811:HKBME;1;0;1;811'HIVISS:164:1:4+1+1+1+1;L;;\xdcberw"
 b'eisung??;;;;2;L;;Dauerauftrag;;;;2;L;;\xe4ndern??;;;;3;L;;Dauerauftrag??;;;'
 b';4;L;;Dauerauftrag;;;;4;L;;l\xf6schen??;;;;5;L;;DA-Aussetzung;;;;5;L;;bearb'
 b'eiten??;;;;6;L;;Termin-;;;;6;L;;\xfcberweisung??;;;;7;L;;Termin\xfcberwei-'
 b';;;;7;L;;sung \xe4ndern??;;;;8;L;;Termin\xfcberwei-;;;;8;L;;sung l\xf6sch'
 b'en??;;;;9;L;;\xdcbertrag??;;;;10;L;;Lastschrift-;;;;10;L;;widerspruch??;;;;'
 b'11;L;;Sammel-;;;;11;L;;lastschrift??;;;;12;L;;Einzel-;;;;12;L;;lastschrift??'
 b';;;;13;L;;Betrag?:;;;;13;R;16;#;;;;14;L;;IBAN Empf\xe4nger?:;;;;14;R;10;#;;'
 b';;15;L;;Konto Empf\xe4nger?:;;;;15;R;10;#;;;;16;L;;Konto Zahler?:;;;;16;R;1'
 b'0;#;;;;17;L;;Anzahl Posten?:;;;;17;R;4;#;;;;18;L;;IBAN Zahler?:;;;;18;R;10;#'
 b';;;;19;L;;Betrag Vorkomma?:;;;;19;R;16;#;;;;20;L;;Abo-Ladeauftrag;;;;20;L;;a'
 b'nlegen??;;;;21;L;;Abo-Ladeauftrag;;;;21;L;;l\xf6schen??;;;;22;L;;Abo-Ladeau'
 b'ftrag;;;;22;L;;\xe4ndern??;;;;23;L;;Kartennummer?:;;;;23;R;10;#;;;;24;L;;An'
 b'meldename;;;;24;L;;\xe4ndern??;;;;25;L;;Anmeldename;;;;25;L;;l\xf6schen??;'
 b';;;26;L;;FondsSparplan;;;;26;L;;l\xf6schen??;;;;27;L;;FondsSparplan;;;;27;L'
 b';;\xe4ndern??;;;;28;L;;ISIN?:;;;;28;R;12;#;;;;29;L;;Depot?:;;;;29;R;10;#;;;'
 b';30;L;;Wertpapier-;;;;30;L;;auftrag l\xf6schen??;;;;31;L;;Wertpapier-;;;;31'
 b';L;;auftrag??;;;;32;L;;FondsSparplan;;;;32;L;;neu??;;;;33;L;;Autorisierung;;'
 b';;33;L;;Direkthandel??;;;;34;L;;WKN / ISIN?:;;;;34;R;12;#;;;;35;L;;L\xe4nde'
 b'rfreischal-;;;;35;L;;tung verwalten??;;;;36;L;;Auslandseinsatz;;;;36;L;;sper'
 b'ren/entsper??;;;;37;L;;Postfachkonten;;;;37;L;;verwalten??;;;;38;L;;Gutschei'
 b'nkauf??;;;;39;L;;DSRZ-Datei;;;;39;L;;freigeben??;;;;40;L;;DSRZ-Datei;;;;40;L'
 b';;l\xf6schen??;;;;41;L;;EU-\xdcberweisung??;;;;42;L;;Auslands-;;;;42;L'
 b';;\xfcberweisung??;;;;43;L;;Konto/IBAN?:;;;;43;R;10;#;;;;44;L;;Sammel-;;;;4'
 b'4;L;;\xfcberweisung??;;;;45;L;;term. Sammel-;;;;45;L;;\xfcberweisung??;;;;'
 b'46;L;;term. Sammel-;;;;46;L;;\xfcberw. l\xf6schen??;;;;47;L;;Eil\xfcberwe'
 b'isung??;;;;48;L;;Festpreisorder??;;;;49;L;;Mitteilung??;;;;50;L;;Einzel-;;;;'
 b'50;L;;lastschrift??;;;;51;L;;Neuemission;;;;51;L;;zeichnen??;;;;52;L;;Handy-'
 b'Aufladung??;;;;53;L;;Mobil Nr.?:;;;;53;R;16;#;;;;54;L;;Wertpapier-;;;;54;L;;'
 b'fondsorder??;;;;55;L;;Wertpapierorder;;;;55;L;;\xe4ndern??;;;;56;L;;Wertpap'
 b'ierorder??;;;;57;L;;Wertpapierorder;;;;57;L;;streichen??;;;;58;L;;Adress'
 b'\xe4nderung??;;;;59;L;;Deka-Depot;;;;59;L;;freischalten??;;;;60;L;;Kontowec'
 b'ker;;;;60;L;;registrieren??;;;;61;L;;Produktverkauf??;;;;62;L;;Produktverkau'
 b'f??;;;;63;L;;Auftragstitel?:;;;;63;L;16;#;;;;64;L;;Kauf Sorten und;;;;64;L;;'
 b'Edelmetalle??;;;;65;L;;Auftrag;;;;65;L;;senden??;;;;66;L;;Konto/IBAN?:;;;;66'
 b';L;16;#;;;;67;L;;IBAN Empf\xe4nger?:;;;;67;L;16;#;;;;68;L;;Freigabe;;;;68;L'
 b';;des Auftrags?:;;;;69;L;;L\xf6schen;;;;69;L;;des Auftrags??;;;;70;L;32;#;;'
 b';;71;L;;Einzelauftrag;;;;71;L;;Ausland??;;;;72;L;;paydirekt;;;;72;L;;Registr'
 b'ierung??;;;;73;L;;\xc4nderung;;;;73;L;;paydirekt-Konto??;;;;74;L;;\xc4nd. '
 b'paydirekt;;;;74;L;;Benutzername??;;;;75;L;;\xc4nd. paydirekt;;;;75;L;;Passw'
 b'ort??;;;;76;L;;paydirekt;;;;76;L;;Entsperren??;;;;77;L;;Postfach-L\xf6sch-;'
 b';;;77;L;;regel anlegen??;;;;78;L;;Postfach-L\xf6sch-;;;;78;L;;regel \xe4nd'
 b'ern??;;;;79;L;;Postfach-L\xf6sch-;;;;79;L;;regel l\xf6schen??;;;;80;L;;Eil'
 b'zahlung??;;;:DKALE;1;811;20;;;23;1;3;13;1;7,1;65;;:DKALL;1;811;21;;;65;;:DKA'
 b'LN;1;811;22;;;23;1;3;13;1;7,1;65;;:DKANA;1;811;24;;;65;;:DKANL;1;811;25;;;65'
 b';;:DKDFC;1;811;26;;;28;1;4;29;1;3,1;65;;:DKDFE;1;811;27;;;28;1;4;29;1;3,1;65'
 b';;:DKDFE;2;811;27;;;28;1;4;29;1;3,1;65;;:DKDFL;1;811;30;;;29;1;3,1;65;;:DKDF'
 b'O;1;811;31;;;28;1;5;29;1;4,1;65;;:DKDFO;2;811;31;;;28;1;5;29;1;4,1;65;;:DKDF'
 b'P;1;811;32;;;28;1;4;29;1;3,1;65;;:DKDFP;2;811;32;;;28;1;4;29;1;3,1;65;;:DKDI'
 b'H;1;811;33;;;29;1;2,1;34;1;3,2;65;;:DKGBA;1;811;35;;;23;1;3;65;;:DKGBS;1;811'
 b';36;;;23;1;3;65;;:DKZDF;1;811;39;;;13;1;4,2;65;;:DKZDF;2;811;39;;;13;1;4,2;6'
 b'5;;:DKZDL;1;811;40;;;65;;:DKZDL;2;811;40;;;65;;:HKAUB;5;811;42;;;66;3;T.16;1'
 b'9;3;T.18;65;;:HKBME;1;811;11;;;13;1;3,1;17;4;NbOfTxs.1;65;;:HKBSE;1;811;12;;'
 b';18;4;IBAN.2;13;4;InstdAmt.1;65;;:HKCCM;1;811;44;;;13;1;3,1;17;4;NbOfTxs.1;6'
 b'5;;:HKCCS;1;811;1;;;14;4;IBAN.2;13;4;InstdAmt.1;65;;:HKCDE;1;811;3;;;14;4;IB'
 b'AN.2;13;4;InstdAmt.1;65;;:HKCDL;1;811;4;;;65;;:HKCDN;1;811;2;;;14;4;IBAN.2;1'
 b'3;4;InstdAmt.1;65;;:HKCDU;1;811;5;;;14;4;IBAN.2;13;4;InstdAmt.1;65;;:HKCME;1'
 b';811;45;;;13;1;3,1;17;4;NbOfTxs.1;65;;:HKCML;1;811;46;;;65;;:HKCSA;1;811;7;;'
 b';14;4;IBAN.2;13;4;InstdAmt.1;65;;:HKCSE;1;811;6;;;14;4;IBAN.2;13;4;InstdAmt.'
 b'1;65;;:HKCSL;1;811;8;;;65;;:HKCUM;1;811;9;;;14;4;IBAN.2;13;4;InstdAmt.1;65;;'
 b':HKDMC;1;811;11;;;13;1;3,1;17;4;NbOfTxs.1;65;;:HKDME;1;811;11;;;13;1;3,1;17;'
 b'4;NbOfTxs.1;65;;:HKDSC;1;811;12;;;18;4;IBAN.2;13;4;InstdAmt.1;65;;:HKDSE;1;8'
 b'11;12;;;18;4;IBAN.2;13;4;InstdAmt.1;65;;:HKDSW;1;811;10;;;65;;:HKFPO;1;811;4'
 b'8;;;29;1;2,1;65;;:HKFPO;3;811;48;;;29;1;2,1;65;;:HKKDM;2;811;49;;;65;;:HKKDM'
 b';3;811;49;;;65;;:HKKDM;4;811;49;;;65;;:HKNEZ;1;811;51;;;29;1;2,1;65;;:HKNEZ;'
 b'3;811;51;;;29;1;2,1;65;;:HKPPD;1;811;52;;;13;1;5,1;53;1;4;65;;:HKWFO;1;811;5'
 b'4;;;29;1;2,1;65;;:HKWFO;3;811;54;;;29;1;2,1;65;;:HKWOA;2;811;55;;;29;1;2,1;6'
 b'5;;:HKWOA;4;811;55;;;29;1;2,1;65;;:HKWPO;2;811;56;;;29;1;2,1;65;;:HKWPO;4;81'
 b'1;56;;;29;1;2,1;65;;:HKWPO;5;811;56;;;29;1;2,1;65;;:HKWPS;1;811;57;;;29;1;2,'
 b'1;65;;:DKBVA;1;811;73;;;65;;:DKBVB;1;811;74;;;65;;:DKBVP;1;811;75;;;65;;:DKB'
 b'VR;1;811;72;;;65;;:DKBVR;2;811;72;;;65;;:DKBVE;1;811;76;;;65;;:HKCSU;1;811;8'
 b"0;;;14;4;IBAN.2;13;4;InstdAmt.1;65;;'HIUPA:165:4:4+2233445566+0+0++PERSNR001"
 b"43218765090'HIUPD:166:6:4+0987654321::280:15050500+DE78150505000987654321+33"
 b'44556677+10+EUR+McZeus+Hermes+Sparkassenbuch++HKSAK:1+HKISA:1+HKSSP:1+HKPAE:'
 b'1+HKTSY:1+HKTAB:1+HKTAU:1+HKSPA:1+HKCAZ:1+HKCUB:1+DKPSA:1+DKPSP:1+HKTAN:1+DK'
 b'ANA:1+DKANL:1+DKKBA:1+DKDKL:1+DKBDK:1+HKFRD:1+HKKDM:1+HKKAZ:1+HKKIF:1+HKSAL:'
 b'1+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
 b'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
 b'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
 b'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
 b'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
 b'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
 b'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
 b'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
 b'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
 b'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
 b'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
 b'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
 b'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{"umsltzt"'
 b'?:"2017-12-30-01.12.54.799483"}\'HIUPD:167:6:4+1234567890::280:15050500+D'
 b'E58150505001234567890+2233445566+1+EUR+McZeus+Hermes+IndividualKonto++HKSAK:'
 b'1+HKISA:1+HKSSP:1+HKPAE:1+HKTSY:1+HKTAB:1+HKTAU:1+HKSPA:1+HKCAZ:1+HKCCS:1+HK'
 b'CDB:1+HKCDE:1+HKCDL:1+HKCDN:1+HKCDU:1+HKCSA:1+HKCSB:1+HKCSE:1+HKCSL:1+HKCUB:'
 b'1+HKCUM:1+HKDSB:1+HKDSW:1+HKEKP:1+HKPPD:1+DKPSA:1+DKPSP:1+HKTAN:1+DKANA:1+DK'
 b'ANL:1+DKKBA:1+DKDKL:1+DKBDK:1+DKALE:1+DKALL:1+DKALN:1+DKBAZ:1+DKBVK:1+DKTCK:'
 b'1+DKZDF:1+DKZDL:1+HKFRD:1+HKKDM:1+HKAUB:1+HKKAZ:1+HKKIF:1+HKSAL:1+++++++++++'
 b'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
 b'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
 b'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
 b'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
 b'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
 b'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
 b'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
 b'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
 b'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
 b'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
 b'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
 b'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
 b'++++++++++++++++++++++++++++++{"umsltzt"?:"2018-07-30-11.16.03.582678"}\''
 b"HISYN:168:4:5+oIm3BlHv6mQBAADYgbPpp?+kWrAQA'HNSHA:169:2+1259150''HNHBS:170:1"
 b"+1'")

SIMPLE_EXAMPLE = \
(b'HNHBK:1:3+000000000428+300+430711670077=043999659571CN9D=+2+430711670077=043'
 b"999659571CN9D=:2'HNVSK:998:3+PIN:1+998+1+2::oIm3BlHv6mQBAADYgbPpp?+kWrAQA+1+"
 b"2:2:13:@8@00000000:5:1+280:15050500:hermes:S:0:0+0'HNVSD:999:1+@195@HNSHK:2:"
 b'4+PIN:1+999+9166926+1+1+2::oIm3BlHv6mQBAADYgbPpp?+kWrAQA+1+1+1:999:1+6:10:16'
 b"+280:15050500:hermes:S:0:0'HIRMG:3:2+0010::Nachricht entgegengenommen.+0100:"
 b":Dialog beendet.'HNSHA:4:2+9166926''HNHBS:5:1+2'")