css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://media.licdn.com/dms/image/C4D0BAQFgUVOyMFHq2w/company-logo_200_200/0/1637528467167?e=2147483647&v=beta&t=PXCIvuLLGXSKP1h5ZcT00NmsgPe3cFwAwGCtUTBuzJ0">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://media.licdn.com/dms/image/D4D03AQGKjKCEtWPiXQ/profile-displayphoto-shrink_800_800/0/1670163570237?e=2147483647&v=beta&t=J2o1bATGZMnc-i8pGWua3QUzSe5UFq_olt12ehf-5qU">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''