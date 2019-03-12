sections = [
    'I',
    'II',
    'III',
    'IV',
    'V',
]

def parentCodeByNbs(code):
    if code in sections:
        return '1' 
    else:
        strTmpSemPonto = code.replace('.','')
        strTmp = strTmpSemPonto.rstrip('0')
        
        if len(strTmp) <= 3:
            if int(strTmpSemPonto) < 102:
                return 'I'
            elif int(strTmpSemPonto) < 109:
                return 'II'
            elif int(strTmpSemPonto) < 112:
                return 'III'
            elif int(strTmpSemPonto) < 122:
                return 'IV'
            else:
                return 'V'
                
            
        elif len(strTmp) <= 6:
            if len(strTmp) <= 5:
                strTmp = strTmp[:-(len(strTmp) - 3)]
            else:
                strTmp = strTmp[:-1]
            strTmp = strTmp[0] + '.' + strTmp[1:5]
        else:
            strTmp = strTmp[:-1]
            strTmp = strTmp[0] + '.' + strTmp[1:11]
            if len(strTmp) >= 6:
                strTmp = strTmp[0:6] + '.' + strTmp[6:11]
            
                if len(strTmp) > 9:
                    strTmp = strTmp[0:9] + '.' + strTmp[9:11]
        return strTmp