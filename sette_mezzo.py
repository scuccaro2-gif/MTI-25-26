from random import randint

punteggio_giocatore = 0.0
punteggio_banco = 0.0

carta_giocatore = randint(1,10)
if carta_giocatore > 7:
    punteggio_giocatore = punteggio_giocatore + 0.5
else:
    punteggio_giocatore = punteggio_giocatore + carta_giocatore


carta_del_banco = randint(1,10)
if carta_del_banco >7:
    punteggio_banco = punteggio_banco + 0.5
else:
    punteggio_banco = punteggio_banco + carta_del_banco

print(f"Il banco ha: {punteggio_banco}")
print(f"E' il tuo turno, hai {punteggio_giocatore}")
scelta = input(f"Cosa vuoi fare? (c per carta): ")
scelta = scelta.lower()
print()

while scelta == "c":
    carta_giocatore = randint(1,10)
    print(f"Numero sulla carta: {carta_giocatore}")
    if carta_giocatore > 7:
        punteggio_giocatore = punteggio_giocatore + 0.5
    else:
        punteggio_giocatore = punteggio_giocatore + carta_giocatore

    print(f"Il banco ha: {punteggio_banco}")
    print(f"Il tuo punteggio: {punteggio_giocatore}")

    if punteggio_giocatore > 7.5:
        scelta = "n"
    else:
        scelta = input(f"Cosa vuoi fare? (c per carta): ")

print()

if punteggio_giocatore > 7.5:
    print("Hai sballato, il banco vince!")
    print(f"Punteggio del banco: {punteggio_banco}")
    print(f"Punteggio del giocatore: {punteggio_giocatore}")
else:
    print("Turno del banco")
    print()
    scelta_banco = True

    while scelta_banco = = False   #non si mette == ma si inizializza una variabile
        if punteggio_banco < punteggio_giocatore and punteggio_banco<7.5:
            print("Il banco chiama carta")
            carta_del_banco = randint(1,10)
            print(f"Numero sulla carta: {carta_del_banco}")
            if carta_del_banco > 7:
                punteggio_banco = punteggio_banco + 0.5
            else:
                punteggio_banco = punteggio_banco + carta_del_banco
            print(f"Il banco ha: {punteggio_banco}")
            print(f"Il tuo punteggio: {punteggio_giocatore}")
        else:
            scelta_banco = False
    print()
    if punteggio_banco >= punteggio_giocatore and punteggio_banco <= 7.5:
        print("Il banco ha vinto!")
        print(f"Punteggio del banco: {punteggio_banco}")
        print(f"Punteggio del giocatore: {punteggio_giocatore}")
    else:
        print("Hai vinto!")
        print(f"Punteggio del banco: {punteggio_banco}")
        print(f"Punteggio del giocatore: {punteggio_giocatore}")