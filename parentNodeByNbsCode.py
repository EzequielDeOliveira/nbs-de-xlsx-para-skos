def parentCodeByNbs(code):
        strTmp = code.replace('.','')
        strTmp = strTmp.rstrip('0')
        
        if len(strTmp) <= 3:
            return '1'
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