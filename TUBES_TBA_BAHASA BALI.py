import streamlit as st
import string

st.write(" Selamat Datang di Program kami :D ")
st.write(""" # Selamat Datang di Program """)
st.write("""
# Lexical Analyzer dan Parser
Aplikasi ini bertujuan untuk mengidentifikasi apakah sebuah lexical/token/kata valid sesuai simbol terminal yang didefinisikan dan apakah susunan token/kata sudah memenuhi aturan pada Grammar yang sudah ditentukan.
""")
st.write('Subject: bli , meme , bapa')
st.write('Verb:  meli  , ngae , madagang , madaar ')
st.write('Object: baas , jaja , serombotan')
st.write('Contoh : bli meli jaja')

sentence = st.text_input("Masukkan Kalimat: ", placeholder="Masukkan kalimat Subject Verb Object")
validasi = st.button("Memvalidasi Grammar")

input_string = sentence.lower()+'#'
tokens = sentence.lower().split()
tokens.append('EOS')

# inisialisasi
alphabet_list = list(string.ascii_lowercase)
state_list = ['q1','q2','q3','q4','q5','q6','q7','q8','q9','q10','q11','q12','q13','q14','q15','q16',
            'q17','q18','q19','q20','q21','q22','q23','q24','q25','q26','q27','q28','q29','q30','q31','q32','q33']


transition_table = {}

for state in state_list:
    for alphabet in alphabet_list:
        transition_table[(state, alphabet)] = 'error'
        transition_table[(state, '#')] = 'error'
        transition_table[(state, ' ')] = 'error'

# spasi sebelum input
transition_table['q0', ' '] = 'q0'


#update the transition for the following token : bli
transition_table[('q0', 'b')] = 'q1'
transition_table[('q1', 'l')] = 'q2'
transition_table[('q2', 'i')] = 'q32'


transition_table[('q32', ' ')] = 'q33'
transition_table[('q32', '#')] = 'accept'
transition_table[('q33', ' ')] = 'q33'
transition_table[('q33', '#')] = 'accept'

#transiotion for new token
transition_table[('q33', 'b')] = 'q1'
transition_table[('q33', 'm')] = 'q6'
transition_table[('q33', 'n')] = 'q17'
transition_table[('q33', 'j')] = 'q20'
transition_table[('q33', 's')] = 'q23'

#update the transition for the following token : bapa
transition_table[('q0', 'b')] = 'q1'
transition_table[('q1', 'a')] = 'q3'
transition_table[('q3', 'p')] = 'q5'
transition_table[('q5', 'a')] = 'q32'

transition_table[('q32', ' ')] = 'q33'
transition_table[('q32', '#')] = 'accept'
transition_table[('q33', ' ')] = 'q33'
transition_table[('q33', '#')] = 'accept'

#update the transition for the following token : meme
transition_table[('q0', 'm')] = 'q6'
transition_table[('q6', 'e')] = 'q7'
transition_table[('q7', 'm')] = 'q8'
transition_table[('q8', 'e')] = 'q32'

transition_table[('q32', ' ')] = 'q33'
transition_table[('q32', '#')] = 'accept'
transition_table[('q33', ' ')] = 'q33'
transition_table[('q33', '#')] = 'accept'

#update the transition for the following token : meli
transition_table[('q0', 'm')] = 'q6'
transition_table[('q6', 'e')] = 'q7'
transition_table[('q7', 'l')] = 'q9'
transition_table[('q9', 'i')] = 'q32'

transition_table[('q32', ' ')] = 'q33'
transition_table[('q32', '#')] = 'accept'
transition_table[('q33', ' ')] = 'q33'
transition_table[('q33', '#')] = 'accept'

#update the transition for the following token : madaar
transition_table[('q0', 'm')] = 'q6'
transition_table[('q6', 'a')] = 'q10'
transition_table[('q10', 'd')] = 'q11'
transition_table[('q11', 'a')] = 'q12'
transition_table[('q12', 'a')] = 'q13'
transition_table[('q13', 'r')] = 'q32'

transition_table[('q32', ' ')] = 'q33'
transition_table[('q32', '#')] = 'accept'
transition_table[('q33', ' ')] = 'q33'
transition_table[('q33', '#')] = 'accept'

#update the transition for the following token : madagang
transition_table[('q0', 'm')] = 'q6'
transition_table[('q6', 'a')] = 'q10'
transition_table[('q10', 'd')] = 'q11'
transition_table[('q11', 'a')] = 'q12'
transition_table[('q12', 'g')] = 'q14'
transition_table[('q14', 'a')] = 'q15'
transition_table[('q15', 'n')] = 'q16'
transition_table[('q16', 'g')] = 'q32'

transition_table[('q32', ' ')] = 'q33'
transition_table[('q32', '#')] = 'accept'
transition_table[('q33', ' ')] = 'q33'
transition_table[('q33', '#')] = 'accept'

#update the transition for the following token : ngae
transition_table[('q0', 'n')] = 'q17'
transition_table[('q17', 'g')] = 'q18'
transition_table[('q18', 'a')] = 'q19'
transition_table[('q19', 'e')] = 'q32'


transition_table[('q32', ' ')] = 'q33'
transition_table[('q32', '#')] = 'accept'
transition_table[('q33', ' ')] = 'q33'
transition_table[('q33', '#')] = 'accept'

#update the transition for the following token : baas
transition_table[('q0', 'b')] = 'q1'
transition_table[('q1', 'a')] = 'q3'
transition_table[('q3', 'a')] = 'q4'
transition_table[('q4', 's')] = 'q32'


transition_table[('q32', ' ')] = 'q33'
transition_table[('q32', '#')] = 'accept'
transition_table[('q33', ' ')] = 'q33'
transition_table[('q33', '#')] = 'accept'

#update the transition for the following token : jaja
transition_table[('q0', 'j')] = 'q20'
transition_table[('q20', 'a')] = 'q21'
transition_table[('q21', 'j')] = 'q22'
transition_table[('q22', 'a')] = 'q32'


transition_table[('q32', ' ')] = 'q33'
transition_table[('q32', '#')] = 'accept'
transition_table[('q33', ' ')] = 'q33'
transition_table[('q33', '#')] = 'accept'

#update the transition for the following token : serombotan
transition_table[('q0', 's')] = 'q23'
transition_table[('q23', 'e')] = 'q24'
transition_table[('q24', 'r')] = 'q25'
transition_table[('q25', 'o')] = 'q26'
transition_table[('q26', 'm')] = 'q27'
transition_table[('q27', 'b')] = 'q28'
transition_table[('q28', 'o')] = 'q29'
transition_table[('q29', 't')] = 'q30'
transition_table[('q30', 'a')] = 'q31'
transition_table[('q31', 'n')] = 'q32'


transition_table[('q32', ' ')] = 'q33'
transition_table[('q32', '#')] = 'accept'
transition_table[('q33', ' ')] = 'q33'
transition_table[('q33', '#')] = 'accept'

# definition untuk simbol non-terminal dan simbol terminal
non_terminal = ['S' ,'SU', 'V', 'O']
terminals = ['bli', 'meme', 'bapa', 'meli', 'ngae', 'madagang', 'madaar', 'baas', 'jaja', 'serombotan']

# definition untuk parse table
parse_table = {}

parse_table[('S', 'bli')] = ['SU', 'V', 'O']
parse_table[('S', 'meme')] = ['SU', 'V', 'O']
parse_table[('S', 'bapa')] = ['SU', 'V', 'O']
parse_table[('S', 'meli')] = ['error']
parse_table[('S', 'ngae')] = ['error']
parse_table[('S', 'madagang')] = ['error']
parse_table[('S', 'madaar')] = ['error']
parse_table[('S', 'baas')] = ['error']
parse_table[('S', 'jaja')] = ['error']
parse_table[('S', 'serombotan')] = ['error']
parse_table[('S', 'EOS')] = ['error']

parse_table[('SU', 'bli')] = ['bli']
parse_table[('SU', 'meme')] = ['meme']
parse_table[('SU', 'bapa')] = ['bapa']
parse_table[('SU', 'meli')] = ['error']
parse_table[('SU', 'ngae')] = ['error']
parse_table[('SU', 'madagang')] = ['error']
parse_table[('SU', 'madaar')] = ['error']
parse_table[('SU', 'baas')] = ['error']
parse_table[('SU', 'jaja')] = ['error']
parse_table[('SU', 'serombotan')] = ['error']
parse_table[('SU', 'EOS')] = ['error']

parse_table[('V', 'bli')] = ['error']
parse_table[('V', 'meme')] = ['error']
parse_table[('V', 'bapa')] = ['error']
parse_table[('V', 'meli')] = ['meli']
parse_table[('V', 'ngae')] = ['ngae']
parse_table[('V', 'madagang')] = ['madagang']
parse_table[('V', 'madaar')] = ['madaar']
parse_table[('V', 'baas')] = ['error']
parse_table[('V', 'jaja')] = ['error']
parse_table[('V', 'serombotan')] = ['error']
parse_table[('V', 'EOS')] = ['error']

parse_table[('O', 'bli')] = ['error']
parse_table[('O', 'meme')] = ['error']
parse_table[('O', 'bapa')] = ['error']
parse_table[('O', 'meli')] = ['error']
parse_table[('O', 'ngae')] = ['error']
parse_table[('O', 'madagang')] = ['error']
parse_table[('O', 'madaar')] = ['error']
parse_table[('O', 'baas')] = ['baas']
parse_table[('O', 'jaja')] = ['jaja']
parse_table[('O', 'serombotan')] = ['serombotan']
parse_table[('O', 'EOS')] = ['error']




# lexical analyzer main program
if validasi:
    idx_char = 0
    state = 'q0'
    current_token = ''
    st.write('Program Lexical')
    st.write(' ')
    while state != 'accept':
        current_char = input_string[idx_char]
        current_token += current_char
        state = transition_table[(state, current_char)]
        if state == 'q32':
            st.write('current token: ', current_token, ', valid')
            current_token = ''
        if state == 'q33':
            st.write('current token: ', current_token, ', valid')
            current_token = ''
        if state == 'error':
            st.write('error')
            break
        idx_char = idx_char + 1

    # conclusion lexical
    if state == 'accept':
        st.write('Semua token di input : ', sentence, ', valid')

    # parser main program

    # Stack initialization
    stack = []
    stack.append('#')
    stack.append('S')

    # Input reading initialization
    idx_token = 0
    symbol = tokens[idx_token]

    # parsing
    st.write('------------------------------------------------')
    st.write('Program Parser')
    while (len(stack) > 0):
        top = stack[len(stack)-1]
        st.write('top= ', top)
        st.write('symbol= ', symbol)
        if top in terminals:
            st.write('top adalah simbol terminal')
            if top == symbol:
                stack.pop()
                idx_token = idx_token+1
                symbol = tokens[idx_token]
                if symbol == 'EOS':
                    st.write('isi stack: ', str(stack))
                    stack.pop()
            else:
                st.write('error')
                break
        elif top in non_terminal:
            st.write('top adalah symbol non-terminal')
            if parse_table[(top, symbol)][0] != 'error':
                stack.pop()
                symbols_to_be_paused = parse_table[(top, symbol)]
                for i in range(len(symbols_to_be_paused)-1, -1, -1):
                    stack.append(symbols_to_be_paused[i])
            else:
                st.write('error')
                break
        else:
            st.write('error')
            break
        st.write('isi stack:', str(stack))
        st.markdown("""---""")

    # conclusion parser
    st.write()
    if symbol == 'EOS' and len(stack) == 0:
        st.success('input string: '+sentence+' valid, sesuai dengan Grammar')
        st.spinner('Mohon Tunggu...')
    else:
        st.error('Error, input string '+sentence+' invalid, tidak sesuai dengan Grammar')