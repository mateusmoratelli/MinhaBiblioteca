import os
import shutil

class FileManager:
    def __init__(self, base_path='.'):
        """
        Inicializa o FileManager com um caminho base.
        """
        self.base_path = os.path.abspath(base_path)



    def create_folder(self, folder_name):
        """
        Verifica se a pasta existe no caminho base; caso não exista, cria.
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
        """
        folder_path = os.path.join(self.base_path, folder_name)
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
        else:
            raise FileNotFoundError(f"Pasta '{folder_name}' não encontrada.")



    def list_files(self, folder_name=None):
        """
        Lista os arquivos em um diretório específico ou no caminho base.
        """
        folder_path = self.base_path if folder_name is None else os.path.join(self.base_path, folder_name)
        if os.path.exists(folder_path):
            return [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        else:
            raise FileNotFoundError(f"Pasta '{folder_path}' não encontrada.")



    def list_folders(self, folder_name=None):
        """
        Lista as subpastas em um diretório específico ou no caminho base.
        """
        folder_path = self.base_path if folder_name is None else os.path.join(self.base_path, folder_name)
        if os.path.exists(folder_path):
            return [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
        else:
            raise FileNotFoundError(f"Pasta '{folder_path}' não encontrada.")



    def copy_file(self, src_file, dest_folder, dest_file):
        """
        Copia um arquivo para uma pasta de destino.
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
        """
        file_path = os.path.join(self.base_path, file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            raise FileNotFoundError(f"Arquivo '{file_name}' não encontrado.")



    def read_file(self, file_name):
        """
        Lê o conteúdo de um arquivo de texto.
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
        """
        file_path = os.path.join(self.base_path, file_name)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        return file_path
