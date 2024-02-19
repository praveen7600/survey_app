from cs50 import SQL

db = SQL("sqlite:///survey.db")

# detials = {'ABINAYA': {'roll': '1', 'mail': 'abivg7132@gmail.com', 'pw': '1243'}, 'AJITH': {'roll': '2', 'mail': 'ajithmbose33@gmail.com', 'pw': '1951'}, 'AKSHARA': {'roll': '3', 'mail': 'kkaksharashreejha@gmail.com ', 'pw': '4805'}, 'PRIGES': {'roll': '4', 'mail': 'priges123@gmail.com', 'pw': '5879'}, 'AB': {'roll': '5', 'mail': 'rajavalliarun@gmail.com', 'pw': '1326'}, 'ARUNMATHAVAN': {'roll': '6', 'mail': 'arunmathavankamaraj2003@gmail.com', 'pw': '2713'}, 'BANUMATHI': {'roll': '7', 'mail': 'banumathi30032003@gmail.com', 'pw': '4623'}, 'CHANDRU': {'roll': '8', 'mail': 'chandrus200211@gmail.com', 'pw': '1594'},  'NIMAL': {'roll': '9', 'mail': 'chiristonimal@gmail.com', 'pw': '9916'}, 'GB': {'roll': '10', 'mail': 'gb1872002@gmail.com', 'pw': '2786'}, 'GEMSHA': {'roll': '11', 'mail': 'gemshadevamiraclin@gmail.com', 'pw': '6754'}, 'HARIHARAN': {'roll': '12', 'mail': 'haran9606@gmail.com', 'pw': '6101'}, 'HARRISH': {'roll': '14', 'mail': 'lmharrish14@gmail.com', 'pw': '9199'}, 'HARSIKA': {'roll': '15', 'mail': 'harsusivakumar06@gmail.com', 'pw': '2619'}, 'INDIRA': {'roll': '16', 'mail': 'indiragandhi2082003@gmail.com', 'pw': '7293'}, 'JAYANTHAN': {'roll': '17', 'mail': 'jayanthandrj@gmail.com', 'pw': '5124'}, 'JUMANA': {'roll': '18', 'mail': 'mjumanamuneera2019@gmail.com', 'pw': '7846'}, 'KALPANA': {'roll': '19', 'mail': 'kalpanakalps357@gmail.com', 'pw': '4524'}, 'KANNAN': {'roll': '20', 'mail': 'therikannan760@gmail.com', 'pw': '2012'}, 'KARTHICK': {'roll': '21', 'mail': 'karthickvikraman5@gmail.com', 'pw': '3200'}, 'KEERTHIKA': {'roll': '22', 'mail': 'keerthika85111@gmail.com', 'pw': '7967'}, 'KENISHIYA': {'roll': '23', 'mail': 'kenishiya5@gmail.com', 'pw': '9853'}, 'MAGESH': {'roll': '25', 'mail': 'magesh20103@gmail.com', 'pw': '6969'}, 'FENCY': {'roll': '27', 'mail': 'fencyj854@gmail.com', 'pw': '4845'}, 'JASMINE': {'roll': '28', 'mail': 'maryjasminejas@gmail.com', 'pw': '2498'},'ISHAAQ': {'roll': '29', 'mail': 'ishaaqmeeran1@gmail.com', 'pw': '1986'}, 'MURSHIDHA': {'roll': '30', 'mail': 'pmh.ihsan@gmail.com ', 'pw': '3324'}, 'MUSITHA': {'roll': '31', 'mail': 'musiselfha@gmail.com', 'pw': '1709'}, 'RETHINA': {'roll': '32', 'mail': 'nagarethina.ar@gmail.com', 'pw': '3172'}, 'NIRMAL': {'roll': '33', 'mail': 'nirmalkumar41332@gmail.com', 'pw': '6186'}, 'PANNEER': {'roll': '34', 'mail': 'panneersubramanian19@gmail.com', 'pw': '9587'}, 'PRAVEEN': {'roll': '35', 'mail': 'praveenking7600@gmail.com', 'pw': '6217'}, 'PRIYA': {'roll': '36', 'mail': 'priyax40@gmail.com', 'pw': '1607'}, 'RAKSHANAA': {'roll': '37', 'mail': 'rakshanaakumar2@gmail.com', 'pw': '8037'}, 'RAMALAKSHMI': {'roll': '38', 'mail': 'indhiralakshmi0108@gmail.com', 'pw': '2487'}, 'RAMASAMY': {'roll': '39', 'mail': 'ramnambi2003@gmail.com', 'pw': '6475'}, 'REVATHY': {'roll': '40', 'mail': 'revathysrisk@gmail.com', 'pw': '3051'}, 'SANDHYA': {'roll': '41', 'mail': 'ksandhya109@gmail.com', 'pw': '2789'}, 'SANJAY': {'roll': '42', 'mail': 'sanjaykumar6112002@gmail.com ', 'pw': '3384'}, 'SHOBANAA': {'roll': '43', 'mail': 'shobanaa2020@gmail.com', 'pw': '3649'}, 'RAJESH': {'roll': '44', 'mail': 'rajeshwaran1206@gmail.com', 'pw': '1017'}, 'SIVA': {'roll': '45', 'mail': 'siva.karthik0610@gmail.com', 'pw': '1379'}, 'TAMIL': {'roll': '48', 'mail': 'tamilselvan150902@gmail.com', 'pw': '8032'}, 'UMABHARATHI': {'roll': '49', 'mail': 'm.umabharathi123@gmail.com', 'pw': '3059'}, 'VAIDHEHI': {'roll': '50', 'mail': 'vaimalakshmi3301@gmail.com', 'pw': '9664'}, 'VAISHNAVI': {'roll': '51', 'mail': 'vaishusep27@gmail.com', 'pw': '1015'}, 'VASANTHA': {'roll': '52', 'mail': 'karthikvkumar2002@gmail.com ', 'pw': '7571'}, 'VJ': {'roll': '53', 'mail': 'svkumar1055@gmail.com', 'pw': '5201'}, 'ZABI': {'roll': '54', 'mail': 'hlawnchhing4@gmail.com', 'pw': '7653'}, 'AKASH': {'roll': '301', 'mail': 'a.alfinakash1@gmail.com', 'pw': '8475'}, 'ARUL': {'roll': '302', 'mail': 'arulras0241@gmail.com', 'pw': '4767'}, 'KAMESH': {'roll': '303', 'mail': 'vetrikamesh11062002@gmail.com ', 'pw': '5091'}, 'KESAVA': {'roll': '304', 'mail': 'kesavamahesh777@gmail.com', 'pw': '1148'}, 'SARANYA': {'roll': '305', 'mail': 'sivamathisaranya18@gmail.com', 'pw': '3663'}, 'SURESH': {'roll': '306', 'mail': 'sureshsuresh32332@gmail.com', 'pw': '5138'}, 'SHAKITHYA': {'roll': '705', 'mail': 'shakithya05@gmail.com', 'pw': '7585'}, 'CHRISTAL': {'roll': '704', 'mail': 'aarkachristalsujaag@gmail.com', 'pw': '9060'}, 'ASHA': {'roll': '702', 'mail': 'ashasm2002@gmail.com', 'pw': '2285'}, 'SIVARANJANI': {'roll': '703', 'mail': 'vranjani2001@gmail.com', 'pw': '4514'}, 'NIBYSHA': {'roll': '706', 'mail': 'nibyshahillary@gmail.com', 'pw': '4237'}, 'RIJOE ': {'roll': '701', 'mail': 'tsrijo444@gmail.com', 'pw': '8815'}}
# i=0
# for name in detials:
#     i+=1
#     data = detials[name]
#     db.execute("INSERT INTO StudentD VALUES (?,?,?, ?, ?)", i,data['roll'], name, data['mail'], data['pw'])

# for i in range(1,62):
 #   db.execute("INSERT INTO compd values (?,0)", i)


#print(db.execute("select q11 from rawsurveydata where ssno=?",5)[0]['Q11'])



#subjects=['DBMS', 'MATHS', 'OS', 'CA', 'DAA', 'SE']
# Assuming SSNo is the first column in your rawsurveydata table
for i in range(1, 63):
    db.execute("INSERT OR REPLACE INTO rawsurveydata(ssno) values (?)", i)





