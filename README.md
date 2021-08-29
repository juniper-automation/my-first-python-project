# Junos Configuration Backup tool
Python script to download Juniper device configs


#  Installation [Your First Python Project](https://www.youtube.com/watch?v=GHujl7c_-hg&t=7481s) Notes

firs thing I did was to Clone the git repo:

```sh
 ~/Documents/GIT
> git clone git@github.com:juniper-automation/my-first-python-project.git
Cloning into 'my-first-python-project'...
The authenticity of host 'github.com (140.82.121.4)' can't be established.
RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'github.com,140.82.121.4' (RSA) to the list of known hosts.
remote: Enumerating objects: 37, done.
remote: Counting objects: 100% (37/37), done.
remote: Compressing objects: 100% (26/26), done.
remote: Total 37 (delta 6), reused 34 (delta 6), pack-reused 0
Receiving objects: 100% (37/37), 27.93 KiB | 357.00 KiB/s, done.
Resolving deltas: 100% (6/6), done.
```

Then I went into the directory containing my first Python project and created a new branch called: my-readme-update.

```sh
 ~/Documents/GIT
> cd my-first-python-project
> git checkout -b my-readme-update
Switched to a new branch 'my-readme-update'
 ~/Documents/GIT/my-first-python-project/my-readme-update
```

I quickly confirm that I am in the branch my-readme-update by running git status.

 ```sh
 > git status
On branch my-readme-update
nothing to commit, working tree clean
 ```

### Running App.py Using [Poetry](https://youtu.be/GHujl7c_-hg?t=3616)

I had to install [poetry](https://formulae.brew.sh/formula/poetry) 

```sh
> brew install poetry
```

Once installed, I was able to activate my Python environment using the poetry shell command line interface.

```sh
> poetry shell
Creating virtualenv my-first-python-project-NEWmLQ26-py3.9 in /Users/vcapp/Library/Caches/pypoetry/virtualenvs
Spawning shell within /Users/vcapp/Library/Caches/pypoetry/virtualenvs/my-first-python-project-NEWmLQ26-py3.9
 ~/Documents/GIT/my-first-python-project/my-readme-update
> . /Users/vcapp/Library/Caches/pypoetry/virtualenvs/my-first-python-project-NEWmLQ26-py3.9/bin/activate
 ~/Documents/GIT/my-first-python-project/my-readme-update
```

I then had to install all of the necessary packages in order to run app.py.

```sh
> poetry install
Installing dependencies from lock file

Package operations: 22 installs, 0 updates, 0 removals

  • Installing pycparser (2.20)
  • Installing cffi (1.14.6)
  • Installing six (1.16.0)
  • Installing bcrypt (3.2.0)
  • Installing cryptography (3.4.8)
  • Installing pynacl (1.4.0)
  • Installing lxml (4.6.3)
  • Installing markupsafe (2.0.1)
  • Installing paramiko (2.7.2)
  • Installing pyyaml (5.4.1)
  • Installing jinja2 (3.0.1)
  • Installing ncclient (0.6.9)
  • Installing netaddr (0.8.0)
  • Installing pyparsing (2.4.7)
  • Installing pyserial (3.5)
  • Installing scp (0.13.6)
  • Installing transitions (0.8.8)
  • Installing yamlordereddictloader (0.4.0)
  • Installing invoke (1.6.0)
  • Installing junos-eznc (2.6.2)
  • Installing jxmlease (1.0.3)
  • Installing python-dotenv (0.19.0)
 ```
 
All of the packages that were made available to me through the *pyproject.toml* file.

```sh
> pip freeze
bcrypt @ file:///Users/vcapp/Library/Caches/pypoetry/artifacts/b9/50/c3/ba3a3f3f202cf25e6e110c6033ca25a523a99a0a7bb2ba160264b448dc/bcrypt-3.2.0-cp36-abi3-macosx_10_9_x86_64.whl
cffi @ file:///Users/vcapp/Library/Caches/pypoetry/artifacts/6e/aa/04/2c3c9401654c8f5580dc8965817a99e8ad464a0987e17149061aadfcbf/cffi-1.14.6-cp39-cp39-macosx_10_9_x86_64.whl
cryptography @ file:///Users/vcapp/Library/Caches/pypoetry/artifacts/35/e0/47/c723b9e84367d9f1138b4fc64ec1a962486221437e37c4e8f99d11827f/cryptography-3.4.8-cp36-abi3-macosx_10_10_x86_64.whl
invoke @ file:///Users/vcapp/Library/Caches/pypoetry/artifacts/a6/91/6d/414821bde1ca707eed52db2a86744992bfa9208d0e6887ee7054139e58/invoke-1.6.0-py3-none-any.whl
Jinja2 @ file:///Users/vcapp/Library/Caches/pypoetry/artifacts/21/2e/46/0a76ea6f6a15e594c9828a85a781f1cee8ed5a1b77e361305645f9e1f4/Jinja2-3.0.1-py3-none-any.whl
junos-eznc @ file:///Users/vcapp/Library/Caches/pypoetry/artifacts/de/b5/8a/9e945ef1b63ed7c158b3b71d1dd45b600702f4e13ae08adaacb07b823f/junos_eznc-2.6.2-py2.py3-none-any.whl
jxmlease @ file:///Users/vcapp/Library/Caches/pypoetry/artifacts/7f/e6/cc/6d218c916ff69736fb7256e9336365c1d1c8ec2a1a4493aee71ccc35f6/jxmlease-1.0.3-py2.py3-none-any.whl
lxml @ file:///Users/vcapp/Library/Caches/pypoetry/artifacts/9e/44/6a/570737853888f173f84e160c5772c792bfd10ea0385a76c138c94b23fc/lxml-4.6.3-cp39-cp39-macosx_10_9_x86_64.whl
MarkupSafe @ file:///Users/vcapp/Library/Caches/pypoetry/artifacts/20/e4/29/5b1a93d4ee8437f01551437cffbb57ba6744c59796443ca99051473f75/MarkupSafe-2.0.1-cp39-cp39-macosx_10_9_x86_64.whl
ncclient @ file:///Users/vcapp/Library/Caches/pypoetry/artifacts/59/12/2f/9d6f536d69629c6706c048f0f474a9a76d50fb09d8e11eca25295b282f/ncclient-0.6.9.tar.gz
netaddr @ file:///Users/vcapp/Library/Caches/pypoetry/artifacts/05/de/10/21e693714d9b24a8d2b2e379b32fc460b450aff988eb114ec5d136dd76/netaddr-0.8.0-py2.py3-none-any.whl
paramiko @ file:///Users/vcapp/Library/Caches/pypoetry/artifacts/5f/6f/fa/6b3207af2c67ec43df657e2b1cdd7906be6450c4641c6fe7111f969a4e/paramiko-2.7.2-py2.py3-none-any.whl
pycparser @ file:///Users/vcapp/Library/Caches/pypoetry/artifacts/37/8e/5a/0ea4f84bc7f11e0e3468110efa2c7783241ea7eaa63a92a751de06f78f/pycparser-2.20-py2.py3-none-any.whl
PyNaCl @ file:///Users/vcapp/Library/Caches/pypoetry/artifacts/d9/af/d1/b0248137a07479e9d1e015704e1ee90dd21592357471dbe32490bee215/PyNaCl-1.4.0-cp35-abi3-macosx_10_10_x86_64.whl
pyparsing @ file:///Users/vcapp/Library/Caches/pypoetry/artifacts/92/0f/cf/effdcd5d76a6186df0969f85b3b030284ff8058936d5016540b5258ea3/pyparsing-2.4.7-py2.py3-none-any.whl
pyserial @ file:///Users/vcapp/Library/Caches/pypoetry/artifacts/a0/11/2a/913bbadee2c313e2b89f80b67f6cfa97e43585bb6f39503aa9453e7053/pyserial-3.5-py2.py3-none-any.whl
python-dotenv @ file:///Users/vcapp/Library/Caches/pypoetry/artifacts/18/b8/a3/8951d0982e502880707d9b287028b0ea076da56ff6171ec458a5fb2aef/python_dotenv-0.19.0-py2.py3-none-any.whl
PyYAML @ file:///Users/vcapp/Library/Caches/pypoetry/artifacts/b6/55/22/537845ea953a4d8d5006f11bdd1b03824425d7f809d5a7ae8efbbeab95/PyYAML-5.4.1-cp39-cp39-macosx_10_9_x86_64.whl
scp @ file:///Users/vcapp/Library/Caches/pypoetry/artifacts/d1/f8/ed/9531c34f31f4d13e8f232ae2374e114c2c069e4787918e84c831686173/scp-0.13.6-py2.py3-none-any.whl
six @ file:///Users/vcapp/Library/Caches/pypoetry/artifacts/08/9f/47/c16ae03035fc69eaf100ea39657a49baaeef714e25a52575710c34cd48/six-1.16.0-py2.py3-none-any.whl
transitions @ file:///Users/vcapp/Library/Caches/pypoetry/artifacts/df/a7/79/b205ee34605b218b697cec99cc3536936c10ac6293f0572c979c24d35d/transitions-0.8.8-py2.py3-none-any.whl
yamlordereddictloader @ file:///Users/vcapp/Library/Caches/pypoetry/artifacts/4e/60/d1/7639f2599833a23a82296958087c6e590fe6b874532720c74534625b76/yamlordereddictloader-0.4.0.tar.gz
 ~/Documents/GIT/my-first-python-project  my-update                                                                                        my-first-python-project-NEWmLQ26-py3.9 py
>
```

## Using [Docker](https://youtu.be/GHujl7c_-hg?t=4892)

It is very simple to install and deploy this application in a Docker container.

in my case I had to install Docker [Desktop](https://docs.docker.com/desktop/mac/install/)  for a MAC with Intell Chip 
```sh
> open ../../../Downloads/Docker.dmg
```
and after the Docker installation was complete

Created a .env file - as it's listed from [.gitignore](https://github.com/juniper-automation/my-first-python-project/blob/main/.gitignore#L1)
and used at line 45 of the Dockerfile  [COPY .env /home/python](https://github.com/juniper-automation/my-first-python-project/blob/main/Dockerfile#L45)


```sh
> touch .env
 ~/Documents/GIT/my-first-python-project/my-readme-update
> docker build -t odb:latest .
[+] Building 1.6s (16/16) FINISHED
 => [internal] load build definition from Dockerfile                                                                                                                             0.0s
 => => transferring dockerfile: 37B                                                                                                                                              0.0s
 => [internal] load .dockerignore                                                                                                                                                0.0s
 => => transferring context: 2B                                                                                                                                                  0.0s
 => [internal] load metadata for docker.io/library/python:3.8-bullseye                                                                                                           1.4s
 => [ 1/11] FROM docker.io/library/python:3.8-bullseye@sha256:a0a734233420b17d9ab37125afc9d8217b75db153d55854ac6683e639f00a8e8                                                   0.0s
 => [internal] load build context                                                                                                                                                0.0s
 => => transferring context: 115B                                                                                                                                                0.0s
 => CACHED [ 2/11] RUN apt update && apt install gcc                                                                                                                             0.0s
 => CACHED [ 3/11] RUN pip install --upgrade pip                                                                                                                                 0.0s
 => CACHED [ 4/11] RUN pip install wheel                                                                                                                                         0.0s
 => CACHED [ 5/11] RUN pip install poetry==1.1.7                                                                                                                                 0.0s
 => CACHED [ 6/11] WORKDIR /home/python                                                                                                                                          0.0s
 => CACHED [ 7/11] COPY poetry.lock pyproject.toml /home/python/                                                                                                                 0.0s
 => CACHED [ 8/11] RUN poetry config virtualenvs.create false                                                                                                                    0.0s
 => CACHED [ 9/11] RUN poetry install --no-interaction --no-ansi                                                                                                                 0.0s
 => CACHED [10/11] COPY app.py /home/python                                                                                                                                      0.0s
 => CACHED [11/11] COPY .env /home/python                                                                                                                                        0.0s
 => exporting to image                                                                                                                                                           0.0s
 => => exporting layers                                                                                                                                                          0.0s
 => => writing image sha256:fb0d11560546419ed1eb17075cd7148cd2c49b67c556c115f57bfa0f27f43684                                                                                     0.0s
 => => naming to docker.io/library/odb:latest                                                                                                                                    0.0s
 ~/Documents/GIT/my-first-python-project  my-readme-update
```

Now I had my Docker Image, which was created based on the parameters specified in the DockerFile.

```sh
> docker images
REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
my-readme    latest    fb0d11560546   4 minutes ago   1.03GB  <<<
```
I can run now the following command

``` > invoke shell ```
can be exucuted if you are inside the poetry Venv
```sh
 ~/Documents/GIT/my-readme-update  main                                                                                               9s  my-first-python-project-N3TcDpri-py3.9 py
> invoke shell
Jumping into container, type exit to return to host
root@bbf8bee31bc6:/home/python# ls
Dockerfile  LICENSE  README.md	app.py	backups  poetry.lock  pyproject.toml  tasks.py
root@bbf8bee31bc6:/home/python#

```


## License

[Apache version 2](https://www.apache.org/licenses/LICENSE-2.0.txt)

**COMMUNITY-LED DEVELOPMENT "THE APACHE WAY"**

