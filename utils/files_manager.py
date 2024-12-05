"""
Arquivo: file_manager.py
Descrição: Classe utilitária para gerenciamento de arquivos e pastas.
Autor: Mateus Moratelli
Data de Criação: 2024-12-04
Última Modificação: 2024-12-04
Detalhes:
    - A classe `FileManager` fornece métodos para operações comuns de manipulação de arquivos e pastas.
    - Funcionalidades incluem:
        - Criação e exclusão de pastas.
        - Listagem de arquivos e subpastas.
        - Operações com arquivos (copiar, mover, deletar).
        - Leitura e escrita de arquivos.
    - A classe foi projetada para trabalhar dentro de um caminho base definido pelo usuário ou padrão (`.`).

Exemplo de uso:
    ```python
    fm = FileManager("/caminho/para/base")
    fm.create_folder("nova_pasta")
    fm.write_file("nova_pasta/arquivo.txt", "Conteúdo de exemplo.")
    arquivos = fm.list_files("nova_pasta")
    print(arquivos)
    fm.delete_file("nova_pasta/arquivo.txt")
    fm.delete_folder("nova_pasta")
    ```
Requisitos:
    - Biblioteca padrão do Python (`os`, `shutil`).
"""


import os
import shutil
import platform
import subprocess

class FileManager:
    def __init__(self, base_path='.'):
        """
        Inicializa o FileManager com um caminho base.
        Este método configura o caminho base onde as operações de gerenciamento de 
        arquivos e pastas serão realizadas. O valor padrão é o diretório atual ('.').
        Args:
            base_path (str): Caminho base para operações de arquivos. O valor 
                            padrão é o diretório atual.
        """
        self.base_path = os.path.abspath(base_path)



    def create_folder(self, folder_name):
        """
        Verifica se a pasta existe no caminho base; caso não exista, cria.
        Este método verifica se a pasta especificada já existe no diretório base.
        Se não existir, ela será criada.
        Args:
            folder_name (str): Nome da pasta a ser criada.
        Returns:
            str: O caminho completo da pasta criada.
        Raises:
            OSError: Se ocorrer algum erro ao criar a pasta.
        """
        folder_path = os.path.join(self.base_path, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Pasta '{folder_path}' criada com sucesso.")
        else:
            print(f"Pasta '{folder_path}' já existe.")
        return folder_path



    def delete_folder(self, folder_name):
        """
        Remove uma pasta e todo o seu conteúdo.
        Este método exclui a pasta e todos os arquivos e subpastas dentro dela, 
        sem pedir confirmação adicional. Caso a pasta não exista, será gerado 
        um erro do tipo FileNotFoundError.
        Args:
            folder_name (str): Nome da pasta que será deletada. Este parâmetro 
                               deve ser o nome da pasta ou o caminho relativo à 
                               pasta base.
        Raises:
            FileNotFoundError: Se a pasta especificada não for encontrada no 
                                diretório base.
            OSError: Se ocorrer algum erro ao remover a pasta.
        """
        folder_path = os.path.join(self.base_path, folder_name)
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
        else:
            raise FileNotFoundError(f"Pasta '{folder_name}' não encontrada.")



    def list_files(self, folder_name=None):
        """
        Lista os arquivos em um diretório específico ou no caminho base.
        Este método retorna uma lista de arquivos no diretório especificado. Se
        o diretório não for fornecido, ele lista os arquivos no caminho base.
        Args:
            folder_name (str, optional): Nome do diretório onde os arquivos 
                                          serão listados. Se não for fornecido, 
                                          a lista será dos arquivos no caminho base.
        Returns:
            list: Lista de nomes de arquivos no diretório especificado.
        Raises:
            FileNotFoundError: Se o diretório especificado não for encontrado.
        """
        folder_path = self.base_path if folder_name is None else os.path.join(self.base_path, folder_name)
        if os.path.exists(folder_path):
            return [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        else:
            raise FileNotFoundError(f"Pasta '{folder_path}' não encontrada.")



    def list_folders(self, folder_name=None):
        """
        Lista as subpastas em um diretório específico ou no caminho base.
        Este método retorna uma lista de subpastas no diretório especificado.
        Se o diretório não for fornecido, ele lista as subpastas no caminho base.
        Args:
            folder_name (str, optional): Nome do diretório onde as pastas serão 
                                          listadas. Se não for fornecido, a lista 
                                          será das pastas no caminho base.
        Returns:
            list: Lista de nomes de subpastas no diretório especificado.
        Raises:
            FileNotFoundError: Se o diretório especificado não for encontrado.
        """
        folder_path = self.base_path if folder_name is None else os.path.join(self.base_path, folder_name)
        if os.path.exists(folder_path):
            return [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
        else:
            raise FileNotFoundError(f"Pasta '{folder_path}' não encontrada.")



    def copy_file(self, src_file, dest_folder, dest_file):
        """
        Copia um arquivo para uma pasta de destino.
        Este método copia um arquivo do diretório base para a pasta de destino 
        especificada. Se a pasta de destino não existir, ela será criada. O arquivo 
        será copiado com o mesmo nome ou com o nome especificado no parâmetro 
        `dest_file`.
        Args:
            src_file (str): Caminho do arquivo de origem a ser copiado.
            dest_folder (str): Nome ou caminho da pasta de destino.
            dest_file (str): Nome do arquivo de destino.
        Returns:
            str: Caminho completo do arquivo copiado.
        Raises:
            FileNotFoundError: Se o arquivo de origem não for encontrado.
            OSError: Se ocorrer algum erro ao copiar o arquivo.
        """
        src_path = os.path.join(self.base_path, src_file)
        dest_path = os.path.join(self.base_path, dest_folder, os.path.basename(dest_file))

        if os.path.exists(src_path):
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.copy2(src_path, dest_path)
            return dest_path
        else:
            raise FileNotFoundError(f"Arquivo '{src_file}' não encontrado.")



    def move_file(self, src_file, dest_folder):
        """
        Move um arquivo para uma pasta de destino.
        Este método move um arquivo do diretório base para a pasta de destino 
        especificada. Se a pasta de destino não existir, ela será criada.
        Args:
            src_file (str): Caminho do arquivo de origem a ser movido.
            dest_folder (str): Nome ou caminho da pasta de destino.
        Returns:
            str: Caminho completo do arquivo movido.
        Raises:
            FileNotFoundError: Se o arquivo de origem não for encontrado.
            OSError: Se ocorrer algum erro ao mover o arquivo.
        """
        src_path = os.path.join(self.base_path, src_file)
        dest_path = os.path.join(self.base_path, dest_folder, os.path.basename(src_file))

        if os.path.exists(src_path):
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.move(src_path, dest_path)
            return dest_path
        else:
            raise FileNotFoundError(f"Arquivo '{src_file}' não encontrado.")



    def delete_file(self, file_name):
        """
        Remove um arquivo.
        Este método exclui um arquivo especificado no diretório base. Caso o arquivo 
        não exista, será gerado um erro do tipo FileNotFoundError.
        Args:
            file_name (str): Nome do arquivo a ser deletado.
        Raises:
            FileNotFoundError: Se o arquivo especificado não for encontrado no diretório base.
            OSError: Se ocorrer algum erro ao excluir o arquivo.
        """
        file_path = os.path.join(self.base_path, file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            raise FileNotFoundError(f"Arquivo '{file_name}' não encontrado.")



    def read_file(self, file_name):
        """
        Lê o conteúdo de um arquivo de texto.
        Este método lê o conteúdo de um arquivo especificado no diretório base. 
        Caso o arquivo não exista, será gerado um erro do tipo FileNotFoundError.
        Args:
            file_name (str): Nome do arquivo a ser lido.
        Returns:
            str: Conteúdo do arquivo lido.
        Raises:
            FileNotFoundError: Se o arquivo especificado não for encontrado.
        """
        file_path = os.path.join(self.base_path, file_name)
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        else:
            raise FileNotFoundError(f"Arquivo '{file_name}' não encontrado.")



    def write_file(self, file_name, content):
        """
        Escreve conteúdo em um arquivo. Se não existir, cria.
        Este método escreve conteúdo em um arquivo no diretório base. Se o arquivo 
        não existir, ele será criado. Se já existir, o conteúdo será sobrescrito.
        Args:
            file_name (str): Nome do arquivo a ser criado ou sobrescrito.
            content (str): Conteúdo a ser escrito no arquivo.
        Returns:
            str: Caminho completo do arquivo criado ou sobrescrito.
        """
        file_path = os.path.join(self.base_path, file_name)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        return file_path



    def abrir_pdf(self, caminho_arquivo: str):
        """
        Abre um arquivo PDF no programa padrão do sistema operacional.
        Este método utiliza o programa padrão configurado no sistema operacional 
        para abrir arquivos PDF. Ele é compatível com Windows, macOS e Linux, 
        utilizando a abordagem apropriada para cada sistema.
        
        Args:
            caminho_arquivo (str): Caminho completo ou relativo do arquivo PDF 
                                que será aberto.

        Raises:
            FileNotFoundError: Se o arquivo especificado não for encontrado no 
                            caminho fornecido.
            Exception: Para outros erros gerais que possam ocorrer ao tentar abrir 
                    o arquivo, como permissões insuficientes ou problemas no 
                    sistema operacional.
        """
        try:
            if platform.system() == "Windows":  # Windows
                os.startfile(caminho_arquivo)
            elif platform.system() == "Darwin":  # macOS
                subprocess.run(["open", caminho_arquivo])
            else:  # Linux/Unix
                subprocess.run(["xdg-open", caminho_arquivo])
        except FileNotFoundError:
            print("Arquivo não encontrado.")
        except Exception as e:
            print(f"Ocorreu um erro ao tentar abrir o arquivo: {e}")