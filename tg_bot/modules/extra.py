import random, re
from random import randint
from telegram import Message, Update, Bot, User
from telegram import MessageEntity
from telegram.ext import Filters, MessageHandler, run_async
from tg_bot.modules.helper_funcs.chat_status import user_admin
from tg_bot.modules.log_channel import loggable
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

ABUSE_STRINGS = (
    "Fuck off",
    "Stfu go fuck yourself",
    "Ur mum gey",
    "Ur dad lesbo",
    "Bsdk",
    "Nigga",
    "Ur granny tranny",
    "you noob",
	"Relax your Rear,ders nothing to fear,The Rape train is finally here",
	"Stfu bc",
	"Stfu and Gtfo U nub",
	"GTFO bsdk"
    "CUnt",
    " Gay is here",
    "Ur dad gey bc ",
    "bahancho"
    
)

EYES = [
    ['⌐■', '■'],
    [' ͠°', ' °'],
    ['⇀', '↼'],
    ['´• ', ' •`'],
    ['´', '`'],
    ['`', '´'],
    ['ó', 'ò'],
    ['ò', 'ó'],
    ['⸌', '⸍'],
    ['>', '<'],
    ['Ƹ̵̡', 'Ʒ'],
    ['ᗒ', 'ᗕ'],
    ['⟃', '⟄'],
    ['⪧', '⪦'],
    ['⪦', '⪧'],
    ['⪩', '⪨'],
    ['⪨', '⪩'],
    ['⪰', '⪯'],
    ['⫑', '⫒'],
    ['⨴', '⨵'],
    ['⩿', '⪀'],
    ['⩾', '⩽'],
    ['⩺', '⩹'],
    ['⩹', '⩺'],
    ['◥▶', '◀◤'],
    ['◍', '◎'],
    ['/͠-', '┐͡-\\'],
    ['⌣', '⌣”'],
    [' ͡⎚', ' ͡⎚'],
    ['≋'],
    ['૦ઁ'],
    ['  ͯ'],
    ['  ͌'],
    ['ළ'],
    ['◉'],
    ['☉'],
    ['・'],
    ['▰'],
    ['ᵔ'],
    [' ﾟ'],
    ['□'],
    ['☼'],
    ['*'],
    ['`'],
    ['⚆'],
    ['⊜'],
    ['>'],
    ['❍'],
    ['￣'],
    ['─'],
    ['✿'],
    ['•'],
    ['T'],
    ['^'],
    ['ⱺ'],
    ['@'],
    ['ȍ'],
    ['  '],
    ['  '],
    ['x'],
    ['-'],
    ['$'],
    ['Ȍ'],
    ['ʘ'],
    ['Ꝋ'],
    [''],
    ['⸟'],
    ['๏'],
    ['ⴲ'],
    ['◕'],
    ['◔'],
    ['✧'],
    ['■'],
    ['♥'],
    [' ͡°'],
    ['¬'],
    [' º '],
    ['⨶'],
    ['⨱'],
    ['⏓'],
    ['⏒'],
    ['⍜'],
    ['⍤'],
    ['ᚖ'],
    ['ᴗ'],
    ['ಠ'],
    ['σ'],
    ['☯']
]

MOUTHS = [
    ['v'],
    ['ᴥ'],
    ['ᗝ'],
    ['Ѡ'],
    ['ᗜ'],
    ['Ꮂ'],
    ['ᨓ'],
    ['ᨎ'],
    ['ヮ'],
    ['╭͜ʖ╮'],
    [' ͟ل͜'],
    [' ͜ʖ'],
    [' ͟ʖ'],
    [' ʖ̯'],
    ['ω'],
    [' ³'],
    [' ε '],
    ['﹏'],
    ['□'],
    ['ل͜'],
    ['‿'],
    ['╭╮'],
    ['‿‿'],
    ['▾'],
    ['‸'],
    ['Д'],
    ['∀'],
    ['!'],
    ['人'],
    ['.'],
    ['ロ'],
    ['_'],
    ['෴'],
    ['ѽ'],
    ['ഌ'],
    ['⏠'],
    ['⏏'],
    ['⍊'],
    ['⍘'],
    ['ツ'],
    ['益'],
    ['╭∩╮'],
    ['Ĺ̯'],
    ['◡'],
    [' ͜つ']
]

EARS = [
    ['q', 'p'],
    ['ʢ', 'ʡ'],
    ['⸮', '?'],
    ['ʕ', 'ʔ'],
    ['ᖗ', 'ᖘ'],
    ['ᕦ', 'ᕥ'],
    ['ᕦ(', ')ᕥ'],
    ['ᕙ(', ')ᕗ'],
    ['ᘳ', 'ᘰ'],
    ['ᕮ', 'ᕭ'],
    ['ᕳ', 'ᕲ'],
    ['(', ')'],
    ['[', ']'],
    ['¯\\_', '_/¯'],
    ['୧', '୨'],
    ['୨', '୧'],
    ['⤜(', ')⤏'],
    ['☞', '☞'],
    ['ᑫ', 'ᑷ'],
    ['ᑴ', 'ᑷ'],
    ['ヽ(', ')ﾉ'],
    ['\\(', ')/'],
    ['乁(', ')ㄏ'],
    ['└[', ']┘'],
    ['(づ', ')づ'],
    ['(ง', ')ง'],
    ['⎝', '⎠'],
    ['ლ(', 'ლ)'],
    ['ᕕ(', ')ᕗ'],
    ['(∩', ')⊃━☆ﾟ.*'],
]

TOSS = ["Result: Heads" , "Result: Tails" ]
mai = ["2","3","4","5","6","7","8","9","10","A","K","J","Q"] 
sec =["♣️","♠️","♥️","♦️"]
mz = ["1","2","3","4","5","6","7","8","9","10"]
b = random.choice(["3","2","3","dot ball","4","2","no ball","1","2","Run out","4","wide ball","1","6","🚾 Wicket 🚾","3","4","2","3","catch out","6","4","3"])

@run_async
def abuse(bot: Bot, update: Update):
    # reply to correct message
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(ABUSE_STRINGS))
	
@run_async
def shrug(bot: Bot, update: Update):
    # reply to correct message
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text("¯\_(ツ)_/¯")	

@loggable
@run_async
@user_admin
def toss(bot: Bot, update: Update):
    x = random.choice(TOSS)
    update.message.reply_text(x)
@loggable
@run_async
@user_admin
def shows(bot: Bot, update: Update):
    x = random.choice(mai)
    z = random.choice(sec)
    c = random.choice(mai)
    p = random.choice(sec)
    l = random.choice(mai)
    g = random.choice(sec)
    update.message.reply_text(x + z)
    update.message.reply_text(c + p)
    update.message.reply_text(l + g)

@loggable
@run_async
@user_admin
def roll(bot: Bot, update: Update):
    x = random.choice(mz)
    update.message.reply_text(x)
@loggable
@run_async
@user_admin
def ball(bot: Bot, update: Update):
    x = random.choice(b)
    update.message.reply_text(x)

@loggable
@run_async
@user_admin
def send(bot: Bot, update: Update):
    # reply to correct message
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(update.effective_message.text.replace("/send",""))
@run_async
def rlg(bot: Bot, update: Update):
    # reply to correct message
    eyes = random.choice(EYES)
    mouth = random.choice(MOUTHS)
    ears = random.choice(EARS)
    repl = format(ears + eyes + mouth + eyes + ears)
    update.message.reply_text(repl)
	
def decide(bot: Bot, update: Update):
        r = randint(1, 100)
        if r <= 65:
            update.message.reply_text("Yes.")
        elif r <= 90:
            update.message.reply_text("NoU.")
        else:
            update.message.reply_text("Maybe.")
            
def table(bot: Bot, update: Update):
            r = randint(1, 100)
            if r <= 45:
                update.message.reply_text("(╯°□°）╯彡 ┻━┻")
            elif r <= 90:
                update.message.reply_text("Send money bsdk to buy new table to flip")
            else:
                update.message.reply_text("Go do some work instead of flippin tables you helpless fagit.")
		
__help__ = """
 - /shrug : get shrug XD.
 - /table : get flip/unflip :v.
 - /decide : Randomly answers yes/no/maybe
 - /abuse : Abuses the cunt
 - /tts <any text> : Converts text to speech
 - /rlg : Join ears,nose,mouth and create an emo ;-;
 - /zal <any text> : zalgofy! your tex Lyrics Plugin will take some moar time to come up.t
 - /send <any text>:  echo something (admin only)
 - /react : get a reaction
 - /gps <place> : get gps location
 - /coin : clip a coin ( toss )
 - /shows : play teen pati
 - /rols : roll Numbers (1 - 10)
 - /bl : play a ball
"""

__mod_name__ = "Extras"

ABUSE_HANDLER = DisableAbleCommandHandler("abuse", abuse)
SHRUG_HANDLER = DisableAbleCommandHandler("shrug", shrug)
RLG_HANDLER = DisableAbleCommandHandler("rlg", rlg)
DECIDE_HANDLER = DisableAbleCommandHandler("decide", decide)
TABLE_HANDLER = DisableAbleCommandHandler("table", table)
ECHO_HANDLER = DisableAbleCommandHandler("send",send)
TOSS_HANDLER = DisableAbleCommandHandler("coin",toss)
TEEN_HANDLER = DisableAbleCommandHandler("shows",shows)
ROLL_HANDLER = DisableAbleCommandHandler("rols",roll)
BALL_HANDLER = DisableAbleCommandHandler("bl",ball)

dispatcher.add_handler(ABUSE_HANDLER)
dispatcher.add_handler(SHRUG_HANDLER)
dispatcher.add_handler(RLG_HANDLER)
dispatcher.add_handler(DECIDE_HANDLER)
dispatcher.add_handler(TABLE_HANDLER)
dispatcher.add_handler(ECHO_HANDLER)
dispatcher.add_handler(TOSS_HANDLER)
dispatcher.add_handler(TEEN_HANDLER)
dispatcher.add_handler(ROLL_HANDLER)
dispatcher.add_handler(BALL_HANDLER)
