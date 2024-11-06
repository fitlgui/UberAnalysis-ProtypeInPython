# Bibliotecas
import customtkinter as ctk

class UberCalculatorApp:
    
    # Inicializa a Janela e o Tamanho dela
    def __init__(self, root):
        self.root = root
        self.root.title("Uber Calculator")
        self.root.geometry("400x400")
        # Chama a interface total
        self.setup_ui()
    
    def setup_ui(self):
        # Configura a interface gráfica
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")
        
        # Cria os campos de entrada para o valor recebido, distância, consumo e custo
        self.ValorRecebidoLabel = ctk.CTkLabel(self.root, text="Valor Recebido:")
        self.ValorRecebidoLabel.pack(pady=5)
        self.valorEntrada = ctk.CTkEntry(self.root)
        self.valorEntrada.pack(pady=5)
        
        self.distanciaLabel = ctk.CTkLabel(self.root, text="Distância (km):")
        self.distanciaLabel.pack(pady=5)
        self.distanciaEntrada = ctk.CTkEntry(self.root)
        self.distanciaEntrada.pack(pady=5)
        
        self.consumoLabel = ctk.CTkLabel(self.root, text="Consumo (km/l):")
        self.consumoLabel.pack(pady=5)
        self.EntradaConsumo = ctk.CTkEntry(self.root)
        self.EntradaConsumo.pack(pady=5)
        
        self.CustoCombustivelLabel = ctk.CTkLabel(self.root, text="Custo do Combustível (R$/l):")
        self.CustoCombustivelLabel.pack(pady=5)
        self.CustoCombustivelEntrada = ctk.CTkEntry(self.root)
        self.CustoCombustivelEntrada.pack(pady=5)
        
        # Botão para calcular o lucro - Chamando método CalculateProfit
        self.botaoCalcular = ctk.CTkButton(self.root, text="Calcular Lucro", command=self.calculateProfit)
        self.botaoCalcular.pack(pady=10)
        
        # Área de exibição do resultado
        self.resultadoLabel = ctk.CTkLabel(self.root, text="")
        self.resultadoLabel.pack(pady=5)
    
    def calculateProfit(self):
        # Tratamento de Erros
        try:
            # Recebe os valores das entradas do usuário
            valorRecebido = float(self.valorEntrada.get())
            distancia = float(self.distanciaEntrada.get())
            consumo = float(self.EntradaConsumo.get())
            CustoCombustivel = float(self.CustoCombustivelEntrada.get())
            
            # Calcula o custo do combustível
            combustivelNecessario = self.calcularCombustivelNecessario(distancia, consumo)
            valorCombustivel = self.calcularPrecoCombustivel(combustivelNecessario, CustoCombustivel)
            
            # Calcula o lucro
            profit = self.calcularValorLiquido(valorRecebido, valorCombustivel)
            
            # Verificação se a Corrida Compensa
            if(profit > 5):
                # Exibe o resultado
                self.resultadoLabel.configure(text=f"Lucro Líquido: R$ {profit:.2f}")
            else:
                # Exibe o resultado
                self.resultadoLabel.configure(text=f"Corrida Não Compensa!")
                                
        except ValueError:
            # Erro caso valores sejam inválidos
            self.resultadoLabel.configure(text="Erro: Por favor, insira valores válidos.")
    
    # Métodos estáticos para chamar sem a necessidade de instanciar.
    
    @staticmethod
    def calcularCombustivelNecessario(distancia, consumo):
        """Calcula a quantidade de combustível necessária."""
        return distancia / consumo
    
    @staticmethod
    def calcularPrecoCombustivel(combustivel, custo):
        """Calcula o custo total de combustível."""
        return combustivel * custo
    
    @staticmethod
    def calcularValorLiquido(valorRecebido, precoCombustivel):
        """Calcula o lucro líquido da corrida."""
        return valorRecebido - precoCombustivel


if __name__ == "__main__":
    root = ctk.CTk()
    app = UberCalculatorApp(root)
    root.mainloop()
