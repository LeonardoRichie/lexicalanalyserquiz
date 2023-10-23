tokens = []
lexemes = []

def keyword(s):
    keyword_list = ['while','int', 'float',  'const', 'main']
    return s in keyword_list

def token(s):
    x = 0
    while x < len(s):
        
        if s[x].isspace():
            x += 1
            
        elif s[x:x+2] == '//':
            x = s.index('\n', x)
            
        elif s[x:x+2] == '/*':
            x = s.index('*/', x) + 2
            
        elif s[x].isalpha():
            y = x + 1
            
            while y < len(s) and (s[y].isalpha() or s[y].isdigit()):
                y += 1
                
            if keyword(s[x:y]):
                
                tokens.append('keyword')
                lexemes.append(s[x:y])
            x = y
            
        else:
            x += 1
            
    return tokens, lexemes

text = 'int main(){const float payment = 384.00;float bal;int month = 0;bal=15000;while (bal>0){printf("Month: %2d Balance: %10.2f\n", month, bal);bal=bal-payment+0.015*bal;month=month+1;}}'

tokens, lexemes = token(text)

for token, lexeme in zip(tokens, lexemes):
    print(token)