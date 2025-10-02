import random

def amongus_simple():
    tripulantes = {"Rojo", "Azul", "Verde", "Amarillo"} 
    
    impostor = random.choice(list(tripulantes))
    
    intentos = 3
    print("🚀 Among Us: 4 tripulantes. Tienes 3 intentos.")
    
    while intentos > 0:
        print(f"\n--- Intento {4 - intentos} de 3 ---")
        print("Tripulantes:")
        
        for i, nombre in enumerate(sorted(list(tripulantes))):
            print(f"  {i+1}. {nombre}")
            
        try:
            eleccion = int(input("¿Quién es el impostor? (1-4): "))
            
            sospechoso = sorted(list(tripulantes))[eleccion - 1]
            
            if sospechoso == impostor:
                print(f"🎉 ¡**Ganaste**! 🎉 **{impostor}** era el impostor.")
                return
            else:
                intentos -= 1
                print(f"❌ {sospechoso} es inocente.")
                
        except (ValueError, IndexError):
            print("⚠️ Entrada inválida. Intenta con un número del 1 al 4.")
            continue
            
    print(f"\n☠️ ¡**Perdiste**! ☠️ Se acabaron los intentos. El impostor era **{impostor}**.")

if __name__ == "__main__":
    amongus_simple()
