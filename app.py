import streamlit as st
import datetime

# ways to print texts
st.title('Hello Geeks, Welcome to GeeksForGeeks')
st.header('Heading')
st.subheader('Subheading')
st.text('Text')

# to write markdown
st.markdown('# Hi')
st.markdown('## Hi')
st.markdown('### Hi')
st.markdown('#### Hi')
st.markdown('##### Hi')
st.markdown('Hi')

# to show banners:
st.success("You have done it!")
st.info('Information')
st.warning('Warning')
st.error('Error!')

# to show exceptional errors:
st.exception(ZeroDivisionError('Div not possible'))
# to show help banner during error encounter:
st.help(ZeroDivisionError)

# to display data:
st.write('range(1,10)')
st.write(range(1,10))
st.write('1+2+3')
st.write(1+2+3)

# to display a code block:
st.code('''x = 11
for i in range(x):
    print(i)''')

# checkbox
st.markdown('#### Checkbox')
agree = st.checkbox('I Agree')
if agree:
 st.write('Great!')

st.markdown('#### Checkbox with fixed no of selections:')
st.write('Select any three values:')
opt1 = st.checkbox('a')
opt2 = st.checkbox('b')
opt3 = st.checkbox('c')
opt4 = st.checkbox('d')
checked = opt1 + opt2 + opt3 + opt4
if checked <3:
 st.error('You have to select atleast 3 options!')
elif checked>3:
 st.error('You have to select only 3 options!')
elif checked == 3:
 st.success('Answer Submitted')

# Radio buttons
st.markdown('#### Radio Buttons:')
radioButton = st.radio('Select Gender:',('Male','Female','Other'))

if(radioButton == 'Male'):
 st.write("You're a Male")
elif(radioButton == 'Female'):
 st.write("You're a Female")
else:
 st.write("You're an Other Gender")

# Select box
st.markdown('#### Select box:')
selected = st.selectbox('Data Science',['Data Analysis','Web Scraping','Deep Learning','Natural Language Processing','Computer Vision','Image Processing'])
st.write("You've selected: ",selected)

# MultiSelect box
st.markdown('#### Mutliselect box:')
multiselct = st.multiselect('Data Science',['Data Analysis','Web Scraping','Deep Learning','Natural Language Processing','Computer Vision','Image Processing'])
st.write("You've selected: ",len(multiselct),'courses')

st.markdown('#### Mutliselect with restrictions:')
multiselct = st.multiselect('Data Science',['Data Analysis','Web Scraping','Deep Learning','Natural Language Processing','Computer Vision','Image Processing'],max_selections=3)
st.write("You've selected: ",len(multiselct),'courses')

# Button
st.markdown('#### Button')
st.button('Click me',type='primary',icon='☺️')
st.button('Click me',type='secondary',icon='🎵')
st.button('Click me',type='tertiary',icon='❤️')
if(st.button('Click me')):
 st.write('Button clicked')

# Slider
st.markdown('#### Slider')
vol = st.slider('Volume',1,100,1)
if(vol):
    st.write('Volume: ',vol)

# Text Input
st.markdown('#### Text Input:')
name = st.text_input('Name: ')
if(name):
    st.write('Hi! ,',name)
usrname = st.text_input('Username: ')
password = st.text_input('Password: ',type='password')

# Textarea
st.markdown('#### TextArea')
text = st.text_area('Write something about yourself in 500 words',height = 100)
st.write(text)

# Input-number
st.markdown('#### Input Number')
age = st.number_input('Enter your name: ',18,110,step = 2)

# Input-date
st.markdown('#### Input Date')
dob = st.date_input('Date of Birth: ',min_value=datetime.date(1990,1,1))
if(dob):
    st.write('Your Birthdate is: ',dob)
# Input-Time
st.markdown('#### Input Time')
st.time_input('Time: ')