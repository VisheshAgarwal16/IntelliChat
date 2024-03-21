import pygame
import time
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 900, 500
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("IntelliCHAT")

mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
BUTTON_WIDTH, BUTTON_HEIGHT = 270, 150

TYPE_SFX = pygame.mixer.Sound("TypeSound.mp3")
RINGTONE_SFX = pygame.mixer.Sound("Ringtone.mp3")

BG_WATERMARK = pygame.transform.scale(pygame.image.load("IntelliCHAT.png"), (300, 300))

HI_BUTTON = pygame.transform.scale(pygame.image.load("Hi.png"), (BUTTON_WIDTH, BUTTON_HEIGHT))
PURPOSE_BUTTON = pygame.transform.scale(pygame.image.load("Purpose.png"), (BUTTON_WIDTH , BUTTON_HEIGHT))
COUNTRY_BUTTON = pygame.transform.scale(pygame.image.load("Country.png"), (BUTTON_WIDTH, BUTTON_HEIGHT))
JOKE_BUTTON = pygame.transform.scale(pygame.image.load("Joke.png"), (BUTTON_WIDTH, BUTTON_HEIGHT))
RIDDLE_BUTTON = pygame.transform.scale(pygame.image.load("Riddle.png"), (BUTTON_WIDTH, BUTTON_HEIGHT))
INDIA_BUTTON = pygame.transform.scale(pygame.image.load("India.png"), (BUTTON_WIDTH, BUTTON_HEIGHT))
FOREIGNER_BUTTON = pygame.transform.scale(pygame.image.load("Foreigner.png"), (BUTTON_WIDTH, BUTTON_HEIGHT))
BYE_BUTTON = pygame.transform.scale(pygame.image.load("Bye.png"), (BUTTON_WIDTH, BUTTON_HEIGHT))

PRESS_KEY_FONT = pygame.font.SysFont("araialblack", 50)
HEADING = pygame.font.SysFont("georgia", 80)
CONVERSATION = pygame.font.SysFont("calibri", 35)
JOKE_RIDDLE_FONT = pygame.font.Font("CalibriBold.ttf", 35)
END_SCREEN_FONT = pygame.font.SysFont("georgia", 35)

def main():
    while True:
        
         SCREEN.fill("white")
         SCREEN.blit(BG_WATERMARK, (SCREEN_WIDTH/2 - 300/2, SCREEN_HEIGHT/2 - 300/2))
         SCREEN.blit(HI_BUTTON, (SCREEN_WIDTH/2 - BUTTON_WIDTH/2, SCREEN_HEIGHT/2 - BUTTON_HEIGHT/2))
         
         key_press = PRESS_KEY_FONT.render("Press SPACE to start a converstion", 1, "black")
         SCREEN.blit(key_press, (SCREEN_WIDTH/2 - key_press.get_width()/2, 350))
         heading = HEADING.render("Welcome to IntelliCHAT", 1, "blue")
         SCREEN.blit(heading, (SCREEN_WIDTH/2 - heading.get_width()/2, 30))
         
         pygame.display.update()
         
         for event in pygame.event.get():
              if event.type == pygame.QUIT:
                   pygame.quit()
              if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_SPACE:
                        intelli()
              
def intelli():

     TYPE_SFX.play()
     time.sleep(2.5)

     while True:
          
        SCREEN.fill("white")
        SCREEN.blit(BG_WATERMARK, (SCREEN_WIDTH/2 - 300/2, SCREEN_HEIGHT/2 - 300/2))
        SCREEN.blit(PURPOSE_BUTTON, (100, SCREEN_HEIGHT/2 - BUTTON_HEIGHT/2 + 50))
        SCREEN.blit(COUNTRY_BUTTON, (800 - BUTTON_WIDTH, SCREEN_HEIGHT/2 - BUTTON_HEIGHT/2 + 50))

        me = CONVERSATION.render("ME: Hi there Intelli. I have some questions for you.", 1, "black")
        SCREEN.blit(me, (10, 10))
        bot = CONVERSATION.render("BOT: Hi User13047695. Glad to see you again. How can I help", 1, "blue")
        SCREEN.blit(bot, (10, 55))
        bot = CONVERSATION.render("you?", 1, "blue")
        SCREEN.blit(bot, (10, 95))
        me = CONVERSATION.render("ME: ...", 1, "black")
        SCREEN.blit(me, (10, 140))
        key_press = PRESS_KEY_FONT.render("Press 'A' for Option1  and  Press 'B' for Option2", 1, "black")
        SCREEN.blit(key_press, (SCREEN_WIDTH/2 - key_press.get_width()/2, 440))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_a:
                      purpose()
                 if event.key == pygame.K_b:
                      origination()

def purpose():

     TYPE_SFX.play()
     time.sleep(2.5)
     
     while True:
        
        SCREEN.fill("white")
        SCREEN.blit(BG_WATERMARK, (SCREEN_WIDTH/2 - 300/2, SCREEN_HEIGHT/2 - 300/2))
        SCREEN.blit(JOKE_BUTTON, (100, SCREEN_HEIGHT/2 - BUTTON_HEIGHT/2 + 50))
        SCREEN.blit(RIDDLE_BUTTON, (800 - BUTTON_WIDTH, SCREEN_HEIGHT/2 - BUTTON_HEIGHT/2 + 50))

        me = CONVERSATION.render("ME: Well, what was the main purpose of making you?", 1, "black")
        SCREEN.blit(me, (10, 10))
        bot = CONVERSATION.render("BOT: As an AI model, my purpose is to assist you to the best ", 1, "blue")
        SCREEN.blit(bot, (10, 55))
        bot = CONVERSATION.render("of my abilities. I can answer questions, engage in conversations", 1, "blue")
        SCREEN.blit(bot, (10, 95))
        bot = CONVERSATION.render("and even entertain you through text messages.", 1, "blue")
        SCREEN.blit(bot, (10, 135))
        me = CONVERSATION.render("ME: ...", 1, "black")
        SCREEN.blit(me, (10, 180))
        key_press = PRESS_KEY_FONT.render("Press 'A' for Option1  and  Press 'B' for Option2", 1, "black")
        SCREEN.blit(key_press, (SCREEN_WIDTH/2 - key_press.get_width()/2, 440))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_a:
                      joke()
                 if event.key == pygame.K_b:
                      riddle()

def origination():
     
     TYPE_SFX.play()
     time.sleep(2.5)
     
     while True:
        
        SCREEN.fill("white")
        SCREEN.blit(BG_WATERMARK, (SCREEN_WIDTH/2 - 300/2, SCREEN_HEIGHT/2 - 300/2))
        SCREEN.blit(INDIA_BUTTON, (100, SCREEN_HEIGHT/2 - BUTTON_HEIGHT/2 + 50))
        SCREEN.blit(FOREIGNER_BUTTON, (800 - BUTTON_WIDTH, SCREEN_HEIGHT/2 - BUTTON_HEIGHT/2 + 50))

        me = CONVERSATION.render("ME: So, where were you first made or programmed?", 1, "black")
        SCREEN.blit(me, (10, 10))
        bot = CONVERSATION.render("BOT: I am AI - based model, and I was first programmed in ", 1, "blue")
        SCREEN.blit(bot, (10, 55))
        bot = CONVERSATION.render("India.", 1, "blue")
        SCREEN.blit(bot, (10, 95))
        me = CONVERSATION.render("ME: ...", 1, "black")
        SCREEN.blit(me, (10, 140))
        key_press = PRESS_KEY_FONT.render("Press 'A' for Option1  and  Press 'B' for Option2", 1, "black")
        SCREEN.blit(key_press, (SCREEN_WIDTH/2 - key_press.get_width()/2, 440))
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_a:
                      india()
                 if event.key == pygame.K_b:
                      foreigner()

def joke():
     
     TYPE_SFX.play()
     time.sleep(2.5)
     
     while True:
        
        SCREEN.fill("white")
        SCREEN.blit(BG_WATERMARK, (SCREEN_WIDTH/2 - 300/2, SCREEN_HEIGHT/2 - 300/2))

        me = CONVERSATION.render("ME: Can you tell me a nice joke?", 1, "black")
        SCREEN.blit(me, (10, 10))
        bot = CONVERSATION.render("BOT: Sure, here's one...", 1, "blue")
        SCREEN.blit(bot, (10, 55))
        bot = JOKE_RIDDLE_FONT.render("Why did the 'scarecrow' win an award?", 1, "red")
        SCREEN.blit(bot, (10, 120))
        bot = JOKE_RIDDLE_FONT.render("Becuase he was 'out-standing' in his field!!", 1, "red")
        SCREEN.blit(bot, (10, 180))
        key_press = PRESS_KEY_FONT.render("Press 'Z' to continue", 1, "black")
        SCREEN.blit(key_press, (SCREEN_WIDTH/2 - key_press.get_width()/2, 440))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_z:
                      end_screen()

def riddle():
          
     TYPE_SFX.play()
     time.sleep(2.5)
     
     while True:
        
        SCREEN.fill("white")
        SCREEN.blit(BG_WATERMARK, (SCREEN_WIDTH/2 - 300/2, SCREEN_HEIGHT/2 - 300/2))

        me = CONVERSATION.render("ME: Ask me a riddle", 1, "black")
        SCREEN.blit(me, (10, 10))
        bot = CONVERSATION.render("BOT: Sure, here's one...", 1, "blue")
        SCREEN.blit(bot, (10, 55))
        bot = JOKE_RIDDLE_FONT.render("I can speak without a mouth and hear without an ear. I don't", 1, "red")
        SCREEN.blit(bot, (10, 120))
        bot = JOKE_RIDDLE_FONT.render("have a body and I come alive with air. What am I??", 1, "red")
        SCREEN.blit(bot, (10, 165))
        bot = JOKE_RIDDLE_FONT.render("An ECHO", 1, "red")
        SCREEN.blit(bot, (10, 225))
        key_press = PRESS_KEY_FONT.render("Press 'Z' to continue", 1, "black")
        SCREEN.blit(key_press, (SCREEN_WIDTH/2 - key_press.get_width()/2, 440))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_z:
                      end_screen()

def india():
               
     TYPE_SFX.play()
     time.sleep(2.5)
     
     while True:
        
        SCREEN.fill("white")
        SCREEN.blit(BG_WATERMARK, (SCREEN_WIDTH/2 - 300/2, SCREEN_HEIGHT/2 - 300/2))

        me = CONVERSATION.render("ME: Hey, I am also from India, nice.", 1, "black")
        SCREEN.blit(me, (10, 10))
        bot = CONVERSATION.render("BOT: Glad to talk to an Indian. We both are from the same ", 1, "blue")
        SCREEN.blit(bot, (10, 55))
        bot = CONVERSATION.render("country. What can be better than this?!", 1, "blue")
        SCREEN.blit(bot, (10, 100))
        bot = CONVERSATION.render("Well, can I know you na...", 1, "blue")
        SCREEN.blit(bot, (10, 145))
        key_press = PRESS_KEY_FONT.render("Press 'Z' to continue", 1, "black")
        SCREEN.blit(key_press, (SCREEN_WIDTH/2 - key_press.get_width()/2, 440))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_z:
                      end_screen()

def foreigner():
                    
     TYPE_SFX.play()
     time.sleep(2.5)
     
     while True:
        
        SCREEN.fill("white")
        SCREEN.blit(BG_WATERMARK, (SCREEN_WIDTH/2 - 300/2, SCREEN_HEIGHT/2 - 300/2))

        me = CONVERSATION.render("ME: Well, I am a foreigner. Nice to meet the Indian AI.", 1, "black")
        SCREEN.blit(me, (10, 10))
        bot = CONVERSATION.render("BOT: Wow, that's good! Nice to meet the first foreigner of", 1, "blue")
        SCREEN.blit(bot, (10, 55))
        bot = CONVERSATION.render("the day. I would love if I could see you.", 1, "blue")
        SCREEN.blit(bot, (10, 100))
        bot = CONVERSATION.render("Well, can I know you na...", 1, "blue")
        SCREEN.blit(bot, (10, 145))
        key_press = PRESS_KEY_FONT.render("Press 'Z' to continue", 1, "black")
        SCREEN.blit(key_press, (SCREEN_WIDTH/2 - key_press.get_width()/2, 440))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_z:
                      end_screen()

def end_screen():

     RINGTONE_SFX.play()
     time.sleep(4)

     run = True
     while run:
          SCREEN.fill("white")
          SCREEN.blit(BYE_BUTTON, (SCREEN_WIDTH/2 - BUTTON_WIDTH/2, SCREEN_HEIGHT/2 - BUTTON_HEIGHT/2 + 100))
          end = END_SCREEN_FONT.render("Excuse Me... Important call", 1, "black")
          SCREEN.blit(end, (10, 10))
          end = END_SCREEN_FONT.render("Actually it was a call from SpaceX.", 1, "blue")
          SCREEN.blit(end, (SCREEN_WIDTH/2 - end.get_width()/2, 100))
          end = END_SCREEN_FONT.render("He invited me join the company so I need to leave.", 1, "blue")
          SCREEN.blit(end, (SCREEN_WIDTH/2 - end.get_width()/2, 150))
          end = END_SCREEN_FONT.render("Bye, hope you have a great day.", 1, "blue")
          SCREEN.blit(end, (SCREEN_WIDTH/2 - end.get_width()/2, 200))
          key_press = PRESS_KEY_FONT.render("Press 'Z' to start again", 1, "black")
          SCREEN.blit(key_press, (SCREEN_WIDTH/2 - key_press.get_width()/2, 440))

          pygame.display.update()

          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    pygame.quit()
               if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_z:
                         main()

if __name__ == "__main__":
     main()