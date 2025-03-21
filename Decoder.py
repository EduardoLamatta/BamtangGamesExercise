message = "Bgc-bfufb tegaedppqna ql aggv zge xof tegaedppfe'l lgjb.\nXof adpf vflqanfe logjbvn'x hf pdwqna d cgebv qn coqro xof tbdkfe ql mjlx d lpdbb tdex. Xof tbdkfe QL XOF HGLL; qx'l kgje vjxk xg fnxfexdqn oqp ge ofe.\nZgrjl ql d pdxxfe gz vfrqvqna codx xoqnal kgj def ngx agqna xg vg.\nXof rglx gz dvvqna d zfdxjef qln'x mjlx xof xqpf qx xdwfl xg rgvf qx. Xof rglx dblg qnrbjvfl xof dvvqxqgn gz dn ghlxdrbf xg zjxjef fstdnlqgn. Xof xeqrw ql xg tqrw xof zfdxjefl xodx vgn'x zqaox fdro gxofe. - Mgon Rdepdrw.\n(ccc.adpdljxed.rgp/uqfc/nfcl/234346?utkjpvbjr)\n(ccc.hedqnkijgxf.rgp/ijgxfl/djxogel/m/mgon_rdepdrw.oxpb)"
freqLang = "TEOAISRHNUCMDLGWFPYKJBVQX"

alphabetMinus = "abcdefghijklmnopqrstuvwxyz"
symbols = "-'.;/?_ \n()"


def AccountingLetters():

    lettersDict = {}
    num = 0

    for letter in alphabetMinus:
        num = 0
        for ch in message:
            if (letter == ch or letter.upper() == ch) and ch not in symbols:
                num += 1   
        if num != 0:
            lettersDict[letter] = num

    return lettersDict
    

def OrganizeLetter():

    organizedDict = {}

    letterDict = AccountingLetters()
    organizedDict = dict(sorted(letterDict.items(), key = lambda x: x[1], reverse = True))

    return organizedDict


def UseFreqLang(freqLangKey):
    
    freqLangDict = {}
    num = 0

    freqLangDict = OrganizeLetter()

    for value in freqLangDict:
        freqLangDict[value] = freqLangKey[num]
        num += 1   
        
    return freqLangDict


def decryptMessage(messageCoded, freqKey):

    messageDecoded = ""
    freqDict = UseFreqLang(freqKey)

    for ch in messageCoded:
        if ch in freqDict:
            messageDecoded += freqDict[ch].lower()

        elif ch.lower() in freqDict:
            messageDecoded += freqDict[ch.lower()]

        else:
            messageDecoded += ch

    return messageDecoded

messageDecoded = decryptMessage(message, freqLang)

print(messageDecoded)



