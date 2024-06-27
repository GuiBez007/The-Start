https://fullcycle.com.br/git-e-github/ <- VER DEPOIS -> https://stackoverflow.com/questions/28429819/rejected-master-master-fetch-first 

         =============================================================
================================ Empty Repository ==========================
         =============================================================\
Quick setup — if you’ve done this kind of thing before or	<RepositoryLink>\
Get started by creating a new file or uploading an existing file. We recommend every repository include a README, LICENSE, and .gitignore\

...or create a new repository on the command line\
echo "apagar" >> README.md\
git add README.md\
git init\
git branch -M main\
git remote add origin -RepositoryLink-\
git add .\
git commit -m "first commit"\
git push -u origin main

...or push an existing repository from the command line\
git remote add origin -RepositoryLink-\
git branch -M main\
git push -u origin main
\==========================================================================
\
\
\
         =============================================================
================================ Main Commands ============================
         =============================================================
INICIAR/DESVINCULAR\
$ git init                            -> (inicializa a pasta - um arquivo oculto ".git" é criado e armazena informações sobre commits)\
$ rm -rf .git                         -> (desreferencia a pasta com o git - desfaz o git init)\

PREPARAR/REMOVER\
$ git add .                           -> (adiciona tudo da pasta ao próximo commit)\
$ git add ArchiveName                 -> (adiciona apenas o especificado)\
$ git reset HEAD -- ArchiveName       -> (remove o especificado dentro do commit feito)\

COMMITAR DIRETO OU NÃO\
$ git commit -m "Mensagem"            -> (commita a pasta preparando-a para o push)\
$ git commit                          -> (abre um bloco para adicionar a mensagem e visualizar tudo antes do commit)\

EMPURRAR/PUXAR\
$ git push                            -> (envia o commit para o repositório no github)\
$ git pull                            -> ("PULLxa" os arquivos do repositório no github)\
\
\
\
OUTROS\
$ git log\
$ git status
\==========================================================================
