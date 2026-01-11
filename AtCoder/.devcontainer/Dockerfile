FROM mcr.microsoft.com/devcontainers/cpp:1-ubuntu-22.04

# システムの更新と必要ツールのインストール
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    python3-pip \
    nodejs \
    npm \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# online-judge-toolsのインストール
RUN pip3 install online-judge-tools selenium

# atcoder-cliのインストール
RUN npm install -g atcoder-cli

# accの設定
RUN acc config default-template cpp

# AtCoder Libraryの配置
RUN git clone https://github.com/atcoder/ac-library.git /opt/ac-library \
    && ln -s /opt/ac-library/atcoder /usr/local/include/atcoder