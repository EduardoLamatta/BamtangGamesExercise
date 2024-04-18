using System;
using System.Collections.Generic;
using System.Linq;


namespace DecryptorProgram
{
    class Decryptor
    {
        /*
         
        Exercise from BamtangGames.com
        Decrypt the next message

        
       "Bgc-bfufb tegaedppqna ql aggv zge xof tegaedppfe'l lgjb.

        Xof adpf vflqanfe logjbvn'x hf pdwqna d cgebv qn coqro xof tbdkfe ql mjlx d lpdbb tdex. Xof tbdkfe QL XOF HGLL; qx'l kgje vjxk xg fnxfexdqn oqp ge ofe.

        Zgrjl ql d pdxxfe gz vfrqvqna codx xoqnal kgj def ngx agqna xg vg.

        Xof rglx gz dvvqna d zfdxjef qln'x mjlx xof xqpf qx xdwfl xg rgvf qx. Xof rglx dblg qnrbjvfl xof dvvqxqgn gz dn ghlxdrbf xg zjxjef fstdnlqgn. Xof xeqrw ql xg tqrw xof zfdxjefl xodx vgn'x zqaox fdro gxofe. - Mgon Rdepdrw.

        (ccc.adpdljxed.rgp/uqfc/nfcl/234346?utkjpvbjr)

        (ccc.hedqnkijgxf.rgp/ijgxfl/djxogel/m/mgon_rdepdrw.oxpb)"


        Si se sabe que solo se han encriptado las letras del alfabeto (a - z).

        Para ello ordena las letras del mensaje encriptado de acuerdo al numero de veces que se repiten (de mayor a menor) y compáralo con la tabla de frecuencia de caracteres del lenguaje en que esta escrito este mensaje, que para este caso es:

        freqLang = "TEOAISRHNUCMDLGWFPYKJBVQX" (de mas frecuente a menos frecuente)

        Implementar la función: decryptMessage( message, freqLang )

        Tu programa debe imprimir el texto desencriptado en pantalla.

        No uses archivos ni pidas ingresar datos.
          
         */

        static void Main(string[] args)
        {

            string messageCrypted = "Bgc-bfufb tegaedppqna ql aggv zge xof tegaedppfe'l lgjb.\r\n\r\nXof adpf vflqanfe logjbvn'x hf pdwqna d cgebv qn coqro xof tbdkfe ql mjlx d lpdbb tdex. Xof tbdkfe QL XOF HGLL; qx'l kgje vjxk xg fnxfexdqn oqp ge ofe.\r\n\r\nZgrjl ql d pdxxfe gz vfrqvqna codx xoqnal kgj def ngx agqna xg vg.\r\n\r\nXof rglx gz dvvqna d zfdxjef qln'x mjlx xof xqpf qx xdwfl xg rgvf qx. Xof rglx dblg qnrbjvfl xof dvvqxqgn gz dn ghlxdrbf xg zjxjef fstdnlqgn. Xof xeqrw ql xg tqrw xof zfdxjefl xodx vgn'x zqaox fdro gxofe. - Mgon Rdepdrw.\r\n\r\n(ccc.adpdljxed.rgp/uqfc/nfcl/234346?utkjpvbjr)\r\n\r\n(ccc.hedqnkijgxf.rgp/ijgxfl/djxogel/m/mgon_rdepdrw.oxpb)";
            string alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ";
            string keyFreqLang = "TEOAISRHNUCMDLGWFPYKJBVQX";
            string messageDecrypted = "";
            Dictionary<char, int> lettersCounted = new Dictionary<char, int>();
            Dictionary<char, char> lettersFreq = new Dictionary<char, char>();
            List<char> listChars = new List<char>(messageCrypted);
            List<char> listFreqLangMayus = new List<char>(keyFreqLang);
            int letterscounter = 0;
            int freqCounter = 0;


            CounterLetters(listChars, alphabet, lettersCounted, letterscounter);

            FreqLetters(lettersCounted, lettersFreq, listFreqLangMayus, freqCounter);

            messageDecrypted = DecryptMessage(messageCrypted, lettersFreq, messageDecrypted);

            Console.WriteLine(messageDecrypted);


        }
        private static Dictionary<char, int> CounterLetters(List<char> listChars, string capitalLetters, Dictionary<char, int> dictlettersCounted, int counter)
        {
            foreach (char c in capitalLetters)
            {
                for (int i = 0; i < listChars.Count; i++)
                {
                    if (char.ToUpper(c) == listChars[i] || char.ToLower(c) == listChars[i]) counter++;
                }
                if (!dictlettersCounted.ContainsKey(c) && counter > 0)
                {
                    dictlettersCounted.Add(c, counter);
                }
                counter = 0;
            }

            return dictlettersCounted;
        }
        private static Dictionary<char, char> FreqLetters(Dictionary<char, int> dictlettersCounted, Dictionary<char, char> dictLetterFreq, List<char> listFreqLang, int counter)
        {
            var orderDict = dictlettersCounted.OrderByDescending(par => par.Value);

            foreach (var kvp in orderDict)
            {
                dictLetterFreq.Add(kvp.Key, listFreqLang[counter]);
                counter++;
            }

            return dictLetterFreq;
        }
        static string DecryptMessage(string statement, Dictionary<char, char> dictLetterFreq, string message)
        {
            foreach (char ch in statement)
            {
                if (char.IsUpper(ch))
                {
                    message += dictLetterFreq[ch];
                }
                else if (char.IsLower(ch))
                {
                    message += char.ToLower(dictLetterFreq[char.ToUpper(ch)]);
                }
                else
                {
                    message += ch;
                }
            }

            return message;
        }
    }
}
