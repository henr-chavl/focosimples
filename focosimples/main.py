import math

def gerar_cronograma(horas_disponiveis, materias):
    if not materias:
        return []
    
    total_pesos = sum(m['prioridade'] for m in materias)
    minutos_totais = horas_disponiveis * 60
    
    cronograma = []
    for m in materias:
        tempo = (m['prioridade'] / total_pesos) * minutos_totais
        cronograma.append({
            "materia": m['nome'],
            "minutos": math.floor(tempo)
        })
    return cronograma

def main():
    print("--- FocoSimples: Organizador de Estudos ---")
    try:
        horas = float(input("Quantas horas você tem hoje? "))
        qtd = int(input("Quantas matérias? "))
        
        materias = []
        for i in range(qtd):
            nome = input(f"Matéria {i+1}: ")
            prioridade = int(input(f"Prioridade (1-5): "))
            materias.append({"nome": nome, "prioridade": prioridade})
            
        plano = gerar_cronograma(horas, materias)
        
        print("\n=== Seu Plano ===")
        for item in plano:
            print(f"📖 {item['materia']}: {item['minutos']} min")
    except (ValueError, ZeroDivisionError):
        print("Erro: Insira valores válidos.")

if __name__ == "__main__":
    main()
