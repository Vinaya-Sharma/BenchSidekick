css = '''
<style>
.chat-container {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.chat-message {
    padding: 1rem;
    border-radius: 0.5rem;
    margin-bottom: 1.5rem;
    display: flex;
    max-width: 70%;
    align-items: center;
}

.fixed-header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    background-color: #ffffff; /* Adjust as needed */
    padding: 10px;
    z-index: 100; /* Ensure the header stays on top */
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1); /* Optional: Add a shadow */
}

.chat-message.user {
    background-color: #2b313e;
    justify-content: flex-end;
    margin-left: auto;
}

.chat-message.bot {
    background-color: #475063;
    justify-content: flex-start;
    margin-right: auto;
}

.chat-message .avatar {
    width: 10%;
    margin-right: 1rem;
}

.chat-message .avatar img {
    max-width: 100%;
    max-height: 50px;
    border-radius: 50%;
    object-fit: cover;
}

.chat-message .message {
    flex-grow: 1;
    padding: 0 1rem;
    color: #fff;
    word-wrap: break-word;
}

.chat-message.user .message {
    background-color: #2b313e;
}

.chat-message.bot .message {
    background-color: #475063;
}

.flex-container {
    display: flex;
    gap:5px
}

</style>
'''

bot_template = '''
<div class="flex-container" >
    <div class="avatar">
        <img src="https://www.clipartmax.com/png/middle/89-896202_medium-image-lowercase-b.png" style="max-height: 50px; max-width: 50px; border-radius: 50%; object-fit: contain;"/>
    </div>
<div class="chat-message bot">
    <div class="message">{{MSG}}</div>
</div>
</div>
'''

user_template = '''
<div class="flex-container">
<div class="chat-message user">
    <div class="message">{{MSG}}</div>
</div>
    <div class="avatar">
        <img src="https://media.licdn.com/dms/image/D5603AQHm-kp9EgdVqg/profile-displayphoto-shrink_800_800/0/1687351029047?e=2147483647&v=beta&t=_Gxo1xTyxVQHldXSk3efWBor4qmSw-pDWAnSLNfQ8k4" style="max-height: 50px; max-width: 50px; border-radius: 50%; object-fit: cover;">
    </div>    
</div>
'''
