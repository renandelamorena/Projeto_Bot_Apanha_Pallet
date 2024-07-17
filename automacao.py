import pyautogui as pag
import pyperclip as pcl
import time

from func import verifica_tela
from func.geral import caminho_absoluto as caminho, pause

pause(0.3)

def click_imagem(caminho_, nome_img):
    verifica_tela.verificar_imagem_encontrada(time.time(), 15, caminho(caminho_), 0.5, nome_img)
    verifica_tela.click(caminho(caminho_), 1)

confirmacao_iniciamento_automacao = pag.confirm(text='Deseja iniciar a automação da Apanha Pallet?', title='Automação Apanha Pallet', buttons=['OK', 'Cancel'])

if confirmacao_iniciamento_automacao == 'OK':

    selec_impressora = None
    while selec_impressora == None:
        selec_impressora = pag.confirm(text='Qual impressora você deseja enviar as etiquetas?', title='Selecione a impressora', buttons=['Pallet', 'Estoque'])

    if selec_impressora == 'Pallet':
        caminho_impressora = 'img/atividade_20/pallet_pallet.png'
        nome_impressora = 'PALLET'

    elif selec_impressora == 'Estoque':
        caminho_impressora = 'img/atividade_20/estoque1_estoque1.png'
        nome_impressora = 'ESTOQUE1'

    pag.alert(text='1. Atividade 20 aberta no Chrome\n2. Impressão de etiquetas aberta em endereço', title='REQUISITOS', button='OK')

    pag.alert(text='Se necessario encerrar a automação, mova o mouse para o canto da tela.', title='ATENÇÃO!', button='OK')

    # 1 Ir ao navegador
    try:
        click_imagem('img/geral/icone_chrome.png', 'icone_chrome')
    except:
        print('Imagem não encontrada (icone_chrome)')

    aceitar = True
    try:
        while aceitar == True:

            # 2 Aceitar atividade
                # selecionar 'Aceitar' (Tempo limite para aceitar)
            click_imagem('img/atividade_20/aceitar.png', 'aceitar - aceitar atividade')

            # 3 Imprimir etiquetas da atividade
                # Click em 'Selecione aqui'
            click_imagem('img/atividade_20/selecione_aqui.png', 'selecione_aqui - seleção da impressora da atividade')

                # Click em (Impressora selecionada acima)
            click_imagem(caminho_impressora, 'Impressora previamente selecionada')

                # Click em 'Confimar'
            click_imagem('img/atividade_20/confirmar_impressao.png', 'confirmar_impressao - confirmar impressao etiqueta da atividade')

            # 4 Guardar e informação da Endereço, tratar e guardar em variavel
                # Click triplo em 'End. Origem:'
            click_imagem('img/atividade_20/end_origem.png', 'end_origem - onde fica o endereço da atividade')
            verifica_tela.click('img/atividade_20/end_origem.png', 2)
            
                # Copiar a informação 'End. Origem: 017-003-04-02'
            pag.hotkey('ctrl', 'c')

                # tratar a informação do end 'End. Origem: 017-003-04-02\r\n' para '010170030402' e guardar em uma variavel
            endereco_copiado = pcl.paste()
            endereco_tratado = '01' + ''.join(filter(str.isdigit, endereco_copiado))

            # 5 Guardar e informação da UMA, tratar e guardar em variavel
                # Click triplo em 'UMA:'
            click_imagem('img/atividade_20/uma.png', 'uma - onde fica a UMA da atividade')
            verifica_tela.click('img/atividade_20/uma.png', 2)

                # Copiar a informação 'UMA: 000000000000168250'
            pag.hotkey('ctrl', 'c')

                # tratar a informação do endereço 'UMA: 000000000000168250\r\n' para '000000000000168250' e guardar em uma variavel
            uma_copiada = pcl.paste()
            uma_tratada = ''.join(filter(str.isdigit, uma_copiada))

            # 6 Guardar e informação da Cód, tratar e guardar em variavel
                # Click triplo em 'Cód.:'
            click_imagem('img/atividade_20/cod.png', 'cod - onde fica o cod da atividade')
            verifica_tela.click('img/atividade_20/cod.png', 2)

                # Copiar a informação 'Cód.: 020000062345'
            pag.hotkey('ctrl', 'c')

                # tratar a informação do endereço 'Cód.: 020000062345\r\n' para '62345' e guardar em uma variavel
            cod_copiado = pcl.paste()
            cod = cod_copiado.replace('Cód.: ', '').replace('\r', '').replace('\n', '')
            cod_tratado = cod[2:].lstrip('0')

            # 7 Confimar informações da atividade
                # Click no campo de 'End. Origem'
            click_imagem('img/atividade_20/campo_end_origem.png', 'campo_end_origem - onde fica o local para colocar endereço na atividade')

                # Colar informação tratada do endereço
            pcl.copy(endereco_tratado)
            pag.hotkey('ctrl', 'v')

            confirmar = True
            while confirmar == True:

                    # Click no campo de 'UMA'
                click_imagem('img/atividade_20/campo_uma.png', 'campo_uma - onde fica o local para colocar UMA na atividade')

                    # Colar informação tratada da UMA
                pcl.copy(uma_tratada)
                pag.hotkey('ctrl', 'v')

                    # Click campo de 'Produto'
                click_imagem('img/atividade_20/campo_produto.png', 'campo_produto - onde fica o local para colocar COD na atividade')

                    # Colar informação tratada de Produto
                pcl.copy(cod_tratado)
                pag.hotkey('ctrl', 'v')

                    # Click no botão 'Confirmar'
                click_imagem('img/atividade_20/confirmar.png', 'confirmar - botão para confirmar atividade')

                    # Click em confirmar denovo 'CONFIRMAR'
                click_imagem('img/atividade_20/confirmar_confirmacao.png', 'confirmar_confirmacao - botão para confirmar a confirmação da atividade')

                time.sleep(5)
                confirmar = verifica_tela.verificar_imagem(caminho('img/atividade_20/confirmar.png'))

                # Confirmar o Box
            click_imagem('img/atividade_20/confirmar_box.png', 'confirmar_box - botão para confirmar o box da atividade')

            # 9 Ir para impressão de etiquetas
            click_imagem('img/geral/icone_impressao_etiqueta.png', 'icone_impressao_etiqueta')

            time.sleep(3)

            # 10 Imprimir etiquetas

                # Colar informação de endereço tratada
            pcl.copy(endereco_tratado)
            pag.hotkey('ctrl', 'v')

                # Click em 'Imprimir'
            click_imagem('img/impressao_etiqueta/imprimir.png', 'imprimir - botão para imprimir')

                # selecionar nome da impressora
            pag.press('right', presses=20)
            pag.press('backspace', presses=20)

            time.sleep(2)

                # Colar nome da impressora
            pcl.copy(nome_impressora)
            pag.hotkey('ctrl', 'v')

                # Click em 'Imprimir'
            pag.press('tab')
            pag.press('enter')

                # voltar para atividade
            click_imagem('img/geral/icone_chrome.png', 'icone_chrome')

            time.sleep(5)
            aceitar = verifica_tela.verificar_imagem(caminho('img/atividade_20/aceitar.png'))
    except:
        pass