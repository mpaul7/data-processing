
"""
This is a list of applcation covered by nDPI static_ip database. 

"""



STATIC_IP_NDPI = [
    'MICROSOFT', 'GOOGLE', 'AMAZON',  'APPLE',  'FACEBOOK',
    'NETFLIX', 'TWITCH','ZOOM', 'SKYPE', 'DROPBOX', 'TELEGRAM', 'WHATSAPP', 'WEBEX', 'DISCORD', 'THREEMA', 'LINE','GOTO',
    
    'BLOOMBERG', 'SUBSCRIBER', 'ALIBABA', 'MS', 'TWITTER', 'VK',  'UBUNTUONE',
    'ROBLOX', 'TENCENT',  'OPENDNS',  'HULU',  'PROTONVPN', 'TOR',  'RIOTGAMES',
    'GITHUB', 'CACHEFLY',  'STEAM', 'CLOUDFLARE', 'NVIDIA', 'CRAWLER', 'STARCRAFT', 
     'EDGECAST', 'DISNEYPLUS' 'ETHEREUM', 'TEAMVIEWER', 'YANDEX', 
    'MULLVAD', 'EPICGAMES', 'AVAST'
    ]

STATIC_IP_MISSING_NDPI = ['bilibioli', 'dailymotion', 'deezer', 'instagram', 'kakao', 'signal', 'netnease', 'slack', 'snaapchat', 
                     'soundcloud', 'spotify', 'tanga', 'tiktok', 'viber', 'wechat', ]

"""
List of ASNs populated from website
https://bgpview.io/ 
"""

"""
List of 20 apps used in twc_v1.5.4
Data: 10-05-2024
"""

new_apps = {
    # douyin
'Venmo': ['AS50477'],
# audible
# alipay
'Stripe': ['AS141743', 'AS394562', 'AS5091', 'AS8838'],
# splashtop
# cloudfare
'Linkedin': ['AS55163', 'AS40793', 'AS20366', 'AS202745', 'AS20049', 'AS14413', 'AS137709', 'AS13443', 'AS132466', 'AS132406'],
# weibo
'Asana' :['AS58303', 'AS57457', 'AS398399', 'AS39330', 'AS31549'],
# Disney plus
'Microsoft Azure' : ['AS14271', 'AS211386',  'AS23536', 'AS24221', 'AS26019', 'AS33447', 'AS397034', 'AS397096', 'AS398100', 'AS398250', 'AS398575', 'AS398656', 'AS398889', 'AS399058', 'AS399583', 'AS400572', 'AS401090', 'AS401093', 'AS401260', 'AS401296'],
'Baidu': ['AS133746', 'AS199506', 'AS38365', 'AS38627', 'AS55967', 'AS63288' ],
# piratebay
# jpush
'Akamai':['AS12222', 'AS133103','AS16625','AS16702','AS17204','AS18680','AS18717','AS20189','AS20940','AS21342','AS21357','AS21399','AS22207','AS22452','AS23454','AS23455','AS23903','AS24319','AS26008','AS30675','AS31107','AS31108','AS31109','AS31110','AS31377','AS33047','AS33905','AS34164','AS34850','AS35204','AS35993','AS35994','AS36183','AS393560','AS39836','AS43639','AS55409','AS55770','AS63949'],
# google_dns
'NextDNS': ['AS34939'],
'TeamViewer': ['AS43304', 'AS212710', 'AS208187', 'AS208175'],
# yahoo_mail
'Quad9': ['AS398892', 'AS398891', 'AS19281' ],
# proton_mail
'DNSFilter':['AS64089'],
'Bing':['AS138832','AS199304', 'AS201529', 'AS207842', 'AS208949', 'AS210008', 'AS210010', 'AS214014', 'AS22401', 'AS393559', 'AS4190', 'AS6933'],
}
ASN = {
    'spotify': ['AS8403'],
    'amazon': ['AS9059', 'AS8987', 'AS801', 'AS7224', 'AS699', 'AS62785', 'AS58588', 'AS40045',
               'AS400098', 'AS399991', 'AS399834', 'AS395343', 'AS39111', 'AS38895', 'AS36263',
               'AS264167', 'AS21664', 'AS19047', 'AS17493', 'AS16509', 'AS14618', 'AS135630',
               'AS10291', 'AS10124'],
    'apple': ['AS714', 'AS63707', 'AS6185', 'AS47995', 'AS400506', 'AS396959', 'AS396918', 'AS35026',
              'AS31128', 'AS2709', 'AS216183', 'AS198675', 'AS150711', 'AS139901', 'AS138575', 'AS136716',
              'AS136581', 'AS11046', 'AS1042', 'AS1036'],
    'youtube': ['AS11344', 'AS1026'],
    'netflix': ['AS55095', 'AS40027', 'AS394406', 'AS2906', 'AS136292'],
    'facebook': ['AS63293', 'AS54115', 'AS34825', 'AS32934', 'AS149642'],
    'skype': ['AS198097'],
    'telegram': ['AS62041', 'AS62014', 'AS59930', 'AS44907', 'AS211157'],
    'whatsapp': ['AS11917'],
    'signal': ['AS397755', 'AS60843'],
    'viber': ['AS271336', 'AS207285'],
    'google': ['AS6432', 'AS55023', 'AS45566','AS43515', 'AS41264', 'AS40873',
               'AS396982', 'AS395973', 'AS394639', 'AS394507', 'AS394089', 'AS36987',
               'AS36561', 'AS36520', 'AS36492', 'AS36411', 'AS36385', 'AS36384', 'AS36383',
               'AS36040', 'AS36039', 'AS32381', 'AS26910', 'AS26684', 'AS22859', 'AS22577',
               'AS19527', 'AS19448', 'AS19425', 'AS16591', 'AS16550', 'AS15169', 'AS13949',
               'AS139190', 'AS139070'],
    'zoom': ['AS46705', 'AS400684', 'AS329157', 'AS31996', 'AS30103', 'AS264449', 'AS205389'
             'AS14220', 'AS140430', 'AS139192', 'AS133433', 'AS132998'],
    'webex': ['AS9450', 'AS6577', 'AS53258', 'AS399937', 'AS26152', 'AS16472', 'AS152185', 'AS139673', 'AS13445'],
    'dropbox': ['AS62190', 'AS54372', 'AS393874', 'AS203719', 'AS200499', 'AS19679'],
}

# IPs not found
# defaultdict(<class 'list'>, {'amazon': ['AS40045', 'AS400098', 'AS399991', 'AS399834', 'AS39111', 'AS38895', 'AS17493',
#             'AS135630', 'AS10291', 'AS10124'], 'apple': ['AS396959', 'AS396918', 'AS150711',
#             'AS1042', 'AS1036'], 'youtube': ['AS1026'], 'netflix': ['AS394406'], 'facebook': ['AS149642'],
#             'skype': ['AS198097'], 'signal': ['AS397755', 'AS60843'], 'google': ['AS55023', 'AS40873', 'AS394639', 'AS394507',
#                 'AS36987', 'AS36520', 'AS36039', 'AS22859', 'AS22577', 'AS19448', 'AS13949'], 'zoom': ['AS46705',
#             'AS400684', 'AS205389AS14220', 'AS139192'], 'webex': ['AS9450', 'AS6577', 'AS16472'], 'dropbox': ['AS393874', 'AS203719']})



ASN_1 = {
    'soundcloud': ['AS197157'],
    'spotify': ['AS8403'],
    'amazon': ['AS9059', 'AS8987', 'AS801', 'AS7224', 'AS699', 'AS62785', 'AS58588', 'AS40045',
               'AS400098', 'AS399991', 'AS399834', 'AS395343', 'AS39111', 'AS38895', 'AS36263',
               'AS264167', 'AS21664', 'AS19047', 'AS17493', 'AS16509', 'AS14618', 'AS135630',
               'AS10291', 'AS10124'],
    'apple': ['AS714', 'AS63707', 'AS6185', 'AS47995', 'AS400506', 'AS396959', 'AS396918', 'AS35026',
              'AS31128', 'AS2709', 'AS216183', 'AS198675', 'AS150711', 'AS139901', 'AS138575', 'AS136716',
              'AS136581', 'AS11046', 'AS1042', 'AS1036'],
    'youtube': ['AS11344', 'AS1026'],
    'netflix': ['AS55095', 'AS40027', 'AS394406', 'AS2906', 'AS136292'],
    'dailymotion': ['AS57068', 'AS41690', 'AS393269', 'AS134607'],
    'twitch': ['AS46489', 'AS397153'],
    'facebook': ['AS63293', 'AS54115', 'AS34825', 'AS32934', 'AS149642'],
    'skype': ['AS198097'],
    'telegram': ['AS62041', 'AS62014', 'AS59930', 'AS44907', 'AS211157'],
    'whatsapp': ['AS11917'],
    'signal': ['AS397755', 'AS60843'],
    'viber': ['AS271336', 'AS207285'],
    'google': ['AS6432', 'AS55023', 'AS45566','AS43515', 'AS41264', 'AS40873',
               'AS396982', 'AS395973', 'AS394639', 'AS394507', 'AS394089', 'AS36987',
               'AS36561', 'AS36520', 'AS36492', 'AS36411', 'AS36385', 'AS36384', 'AS36383',
               'AS36040', 'AS36039', 'AS32381', 'AS26910', 'AS26684', 'AS22859', 'AS22577',
               'AS19527', 'AS19448', 'AS19425', 'AS16591', 'AS16550', 'AS15169', 'AS13949',
               'AS139190', 'AS139070'],
    'snapchat': ['AS395291'],
    'zoom': ['AS46705', 'AS400684', 'AS329157', 'AS31996', 'AS30103', 'AS264449', 'AS205389'
             'AS14220', 'AS140430', 'AS139192', 'AS133433', 'AS132998'],
    'tiktok': ['AS138699'],
    'microsoft': ['AS8812', 'AS8075', 'AS8074', 'AS8073', 'AS8072', 'AS8071', 'AS8071', 'AS8069',
                  'AS8068', 'AS6584', 'AS63314', 'AS63245', 'AS6291', 'AS6194', 'AS6182', 'AS59067',
                  'AS58862', 'AS5761', 'AS52985', 'AS45139', 'AS400884', 'AS40066', 'AS400582',
                  'AS400581', 'AS400580', 'AS400579', 'AS400577', 'AS400576', 'AS400575', 'AS400575',
                  'AS400573', 'AS400572', 'AS398961', 'AS398661', 'AS398659', 'AS398658', 'AS398657',
                  'AS398656', 'AS397996', 'AS397466', 'AS397096', 'AS396463', 'AS395851', 'AS395524', 'AS395496',
                  'AS36006', 'AS3598', 'AS35106', 'AS32476', 'AS31792', 'AS30575', 'AS30135', 'AS26222', 'AS25796',
                  'AS23468', 'AS22692', 'AS200517', 'AS20046', 'AS17345', 'AS14719', 'AS13811', 'AS13399','AS132348',
                  'AS12076'],
    'webex': ['AS9450', 'AS6577', 'AS53258', 'AS399937', 'AS26152', 'AS16472', 'AS152185', 'AS139673', 'AS13445'],
    'gotomeeting': ['AS6643', 'AS395424', 'AS21866', 'AS213380', 'AS20104', 'AS16815', 'AS131943'],
    'dropbox': ['AS62190', 'AS54372', 'AS393874', 'AS203719', 'AS200499', 'AS19679'],
    'line': ['AS7482'], #choose the one related to asia pacific
    'kakaotalk': ['AS9764', 'AS7625', 'AS45991', 'AS38678', 'AS38099', 'AS23588', 'AS18160',
                  'AS152199', 'AS131828', 'AS10158'],
    'tango': ['AS49354', 'AS133415'],
    'ftp': ['AS149811'],
    'scp': ['AS42404', 'AS210086'],
    'alibaba' : ['AS59055', 'AS59054', 'AS59053', 'AS59052', 'AS59051', 'AS59028', 'AS45104', 'AS45103', 'AS45102',
                 'AS37963', 'AS34947', 'AS211914', 'AS134963' ],
    'baidu' : ['AS63729', 'AS63728', 'AS63288', 'AS55967', 'AS45085', 'AS45076', 'AS38627', 'AS38365', 'AS199506',
               'AS133746', 'AS131141', 'AS131140', 'AS131139', 'AS131139'],
    'bbc' : ['AS9156', 'AS34158', 'AS31459', 'AS2818'],
    'bilibili' : ['AS63828', 'AS63828', 'AS140633'],
    'disney' : ['AS8137', 'AS54330', 'AS53578', 'AS46557', 'AS400805', 'AS400558', 'AS400557', 'AS40051',
                'AS400265', 'AS399490', 'AS399344', 'AS398849', 'AS396054', 'AS30311', 'AS30224', 'AS29736',
                'AS25932', 'AS23344', 'AS22604', 'AS205757', 'AS20374', 'AS17122', 'AS15260', 'AS140693', 'AS13379',
                'AS11812', 'AS11251'],
    'ebay' : ['AS11643', 'AS131796', 'AS14494', 'AS24331',  'AS40533', 'AS43193', 'AS43392', 'AS53358', 'AS6907', 'AS60939', 'AS62955', 'AS9424'],
    'foxnews' : ['AS53294'],
    'github' : ['AS36459'],
    'hulu': ['AS23286'],
    'linkedin' : ['AS55163', 'AS40793', 'AS30427', 'AS20366', 'AS202745', 'AS20049', 'AS14413',
                  'AS137709', 'AS13443', 'AS132466', 'AS132406'],
    'meta' : ['AS64269', 'AS43181', 'AS136473'],
    'msn' : ['AS34352', 'AS12790'],
    'pinterest' : ['AS53620'],
    'quora' : ['AS36361'],
    'tidal' : ['AS10769'],
    'twitter' : ['AS8945', 'AS63179', 'AS54888', 'AS35995', 'AS13414'],
    'yahoo': ['AS7233', 'AS58721', 'AS58720', 'AS58525', 'AS55898', 'AS55517', 'AS55418',
              'AS55417', 'AS55416', 'AS45915', 'AS45863', 'AS45502', 'AS45501', 'AS43428',
              'AS42173', 'AS40986', 'AS38072', 'AS38045', 'AS34082', 'AS34010', 'AS28122',
              'AS265584', 'AS24572', 'AS24506', 'AS24376', 'AS24296', 'AS24236', 'AS24018',
              'AS23816', 'AS23663', 'AS204000', 'AS203220', 'AS203219', 'AS203070', 'AS18140',
              'AS15896', 'AS15635', 'AS134706', 'AS131898']
}
ASN_th  = {
        # 'Threema' : ['AS29691'],
        #    'Wechat': ['AS140293'],
        #    'Tango': ['AS10257', 'AS133415', 'AS29893', 'AS32717','AS48526','AS56665'],
        #    'Telegram': ['AS62041', 'AS62014', 'AS59930', 'AS44907', 'AS211157'],
        #    'Viber': ['AS271336', 'AS207285', 'AS142319'],
        #    'Youtube': ['AS11344', 'AS1026', 'AS36040', 'AS36561', 'AS43515'],
            'Baidu': ['AS133746', 'AS199506', 'AS38365', 'AS38627' 'AS55967', 'AS63288'],
            'Disney': ['AS8137', 'AS17122', 'AS53578', 'AS399344', 'AS30224', 'AS20374', 'AS17122'],
            'Kakaotalk': ['AS131858', 'AS38099',  'AS38667', 'AS38678', 'AS45991', 'AS9958', 'AS38099', 'AS152199', 'AS131858'],
            'Twitter' : ['AS8945', 'AS63179', 'AS54888', 'AS35995', 'AS13414'],
            'Linkedin' : ['AS55163', 'AS40793', 'AS30427', 'AS20366', 'AS202745', 'AS20049', 'AS14413', 'AS137709', 'AS13443', 'AS132466', 'AS132406'],
            'Ebay': ['AS11643', 'AS131796', 'AS14494', 'AS24331',  'AS40533', 'AS43193', 'AS43392', 'AS53358', 'AS6907', 'AS60939', 'AS62955', 'AS9424'],
            'Citrix' : ['AS132361', 'AS43204', 'AS60825', 'AS62795'],
            'Outbrain': ['AS22075'],
            'Pinterest': ['AS53620'],
            'Adjust': ['AS205184', 'AS396535', 'AS61273'],
            'Deepintent': ['AS398989', 'AS399183', 'AS401006'],
            'Adform': ['AS198622'],
            'Smartadserver': ['AS201081', 'AS47043'],
            'Bilibili' : ['AS63828', 'AS140943', 'AS140633'],
                }

ASN_old= {
    'facebook': ['AS149642', 'AS32934', 'AS54115', 'AS63293'], 
    'microsoft': ['AS12233','AS13399', 'AS14271', 'AS14719', 'AS20046', 'AS23468', 'AS35106', 'AS3598', 'AS395496', 'AS395524', 'AS395851', 'AS396463',
                  'AS397096', 'AS398575', 'AS398656', 'AS400572', 'AS45139', 'AS52985', 'AS5761', 'AS6182', 'AS6584', 'AS8068', 'AS8069', 'AS8070', 
                  'AS8071', 'AS8075'],
    'google': ['AS139190', 'AS15169', 'AS16550', 'AS16591', 'AS19448', 'AS19527', 'AS200238', 'AS22859', 'AS24424', 'AS264324', 'AS26684', 'AS26910', 'AS32381',
               'AS36039', 'AS36384', 'AS36385', 'AS36492', 'AS36987', 'AS394507', 'AS394639', 'AS395973', 'AS396982', 'AS41264', 'AS55023', 'AS6432'], 
    'amazon': ['AS135630', 'AS14618', 'AS16509', 'AS17493', 'AS262486', 'AS262772', 'AS263639', 'AS264167', 'AS264344', 'AS264509', 'AS266122', 'AS266194',
               'AS267242', 'AS268063', 'AS271017', 'AS271047', 'AS38895', 'AS52994', 'AS58588', 'AS61577', 'AS62785', 'AS699', 'AS7224', 'AS801'], 
    'apple': ['AS1042', 'AS11046', 'AS135855', 'AS136581', 'AS136716', 'AS138575', 'AS139901', 'AS14009', 'AS150711', 'AS198926', 'AS206368', 'AS208629', 
              'AS210443', 'AS216183', 'AS23196', 'AS396918', 'AS396959', 'AS54506', 'AS6185', 'AS63707', 'AS714'], 
    'netflix': ['AS40027', 'AS2906'], 
    'zoom': ['AS139192',  'AS140430', 'AS205389', 'AS264547', 'AS266983', 'AS270225', 'AS30103', 'AS31786', 'AS31996', 'AS328529', 'AS35433', 'AS36016',
             'AS393735', 'AS400684', 'AS42611', 'AS46705', 'AS62137'], 
    'dropbox': ['AS19679', 'AS393874', 'AS54372', 'AS62190'], 
    'telegram': ['AS211157', 'AS44907', 'AS59930', 'AS62014', 'AS62041'], 
    'whatsapp': ['AS11917'], 
    'webex': ['AS10365', 'AS10790', 'AS11615', 'AS152185', 'AS6577', 'AS9450', 'AS9566'], 
    'goto': ['AS141167', 'AS16815',  'AS20104', 'AS208362', 'AS21866', 'AS39673', 'AS52621', 'AS9465'], 
    'dailymotion': ['AS57068', 'AS41690', 'AS393269'], 
    'kakao': ['AS131858', 'AS38099',  'AS38667', 'AS38678', 'AS45991', 'AS9958', 'AS38099', 'AS152199', 'AS131858'], 
    'slack': ['AS32562', 'AS206770'],        
    'soundcloud': ['AS197157'], 
    'spotify': ['AS8403'], 
    'tanga': ['AS61933', 'AS202996', 'AS138114', '	AS138109'], 
    'tiktok': ['AS138699'], 
    'viber': ['AS207285', 'AS142319'], 
    }

ASN_newApps = { 'Venmo': ['AS25478', 'AS1299', 'AS31133' ], 
'Stripe': ['AS141743', 'AS394562', 'AS5091', 'AS8838' ],
'Linkedin': ['AS132406', 'AS132466', 'AS13443', 'AS137709', 'AS14413', 'AS20049', 'AS202745', 'AS20366', 'AS40793',  'AS55163' ],
'Asana': ['AS31549', 'AS39330', 'AS398399', 'AS57457', 'AS58303', ],
'Disney': ['AS17122', 'AS20374', 'AS30224', '	AS399344', 'AS53578', 'AS8137' ],
'Akamai': ['AS12222', 'AS133103', 'AS16625', 'AS16702', 'AS17204', 'AS18680', 'AS18717', 'AS20189', 'AS20940', 'AS21342', 'AS21357', 'AS21399', 'AS22207', 'AS22452', 'AS23454', 'AS23455', 'AS23903', 'AS24319', 'AS26008', 'AS30675', 'AS31107', 'AS31108', 'AS31109', 'AS31110', 'AS31377', 'AS33047', 'AS33905', 'AS34164', 'AS34850', 'AS35204', 'AS35993', 'AS35994', 'AS36183', 'AS393560', 'AS39836', 'AS43639', 'AS55409', 'AS55770', 'AS63949'],
'NextDNS': ['AS34939'],
'Quad9': ['AS19281', 'AS398891', 'AS398892'],
'DNSFilter': ['AS64089']
}
"""
for these applications only IP addresses are avaialble
https://bgpview.io/ 
"""
IP = {'deezer': ['185.159.104.0/22', '185.159.106.0/23'],
      'discord': ['188.244.120.0/24', '195.62.89.0/24','198.186.219.0/24' '66.22.192.0/18', '66.22.228.0/24', '66.22.240.0/24', '66.22.244.0/24', ], 
      'snapchat': ['only IPv6 are available'], 
    
}


"""
Applications with ambiguous search keywords on bgpview.io that make ASN lookup difficult.
For example, searching 'line' returns results for airlines, power lines, etc.
"""
GENERIC = {'signal': [],
           'line': [], }

"""
ASN for these applications is not available on the https://radb.mnet database. Need to find more from RIRs
"""
NOT_AVAILABLE =  {'wechat': [],
                  'netnease': [], 
                  'instagram': [],
                  'billibilli': [], 
                  'threema': [],
                  'twitch': [],
                  'bittorent': []
                  }
