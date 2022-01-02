FROM python:3.6

# ソースを置くディレクトリを変数として格納                                                  
ARG project_dir=/projects/

# 必要なファイルをローカルからコンテナにコピー
ADD requirements.txt $project_dir
ADD app.py $project_dir

# requirements.txtに記載されたパッケージをインストール                         
WORKDIR $project_dir



RUN pip install --upgrade pip
RUN pip install --user -r requirements.txt

EXPOSE 5001

#コマンド実行
CMD ["python", "/projects/app.py"]