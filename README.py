#!/usr/bin/env python
# coding: utf-8

# # Como verificar bad blocks no HD/SSD com o Badblocks, clonar com o `BadBlocks e o Data Duplicator e monitorar com o Smartmontools` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para verificar bad blocks no HD/SSD e clonar com o `Badblocks e o Data Duplicator` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _In this document are contained the main commands and settings to check for bad blocks on the HD/SSD and to clone using `Badblocks and the Data Duplicator` on `Linux Ubuntu`._

# ## Descrição [2]
# 
# ### bad blocks
# 
# Bad blocks, em português "blocos defeituosos," são setores de armazenamento de dados em dispositivos de armazenamento, como discos rígidos (HDDs) e unidades de estado sólido (SSDs), que apresentam falhas ou danos físicos. Esses blocos defeituosos podem resultar em erros de leitura ou gravação de dados, causando perda de informações ou deterioração do desempenho do dispositivo. Para lidar com bad blocks, os sistemas operacionais e utilitários de manutenção de disco geralmente incluem ferramentas de verificação e marcação, que identificam e isolam os blocos defeituosos, evitando que dados sejam gravados neles. Essa gestão de bad blocks ajuda a prolongar a vida útil do dispositivo de armazenamento e a manter a integridade dos dados armazenados.
# 
# ### Data Duplicator
# 
# Data Duplicator, ou "Duplicador de Dados," é uma ferramenta ou processo usado para criar cópias exatas de dados, arquivos ou sistemas. Ele é frequentemente utilizado para fins de backup, recuperação de desastres e replicação de informações em ambientes de TI. O Data Duplicator pode ser implementado por meio de software especializado, hardware dedicado ou até mesmo combinações de ambos. Sua principal função é garantir a preservação dos dados, criando réplicas idênticas que podem ser usadas para restaurar sistemas ou recuperar informações em caso de falhas de hardware, corrupção de dados ou outras situações imprevistas. Esse processo é fundamental para a proteção e disponibilidade de dados críticos em organizações e ambientes de computação.
# 
# ### Smartmontools
# 
# O smartmontools é um conjunto de utilitários de linha de comando de código aberto disponível em sistemas Linux e UNIX, projetado para monitorar e gerenciar discos rígidos (HDDs) e unidades de estado sólido (SSDs) compatíveis com a tecnologia S.M.A.R.T. (Self-Monitoring, Analysis, and Reporting Technology). Essa ferramenta permite aos usuários verificar o estado de saúde de seus dispositivos de armazenamento, incluindo a detecção precoce de possíveis falhas, como setores defeituosos, superaquecimento ou outros problemas que possam afetar a integridade dos dados. O smartmontools fornece informações detalhadas sobre a saúde e o desempenho dos discos e permite que os administradores e usuários tomem medidas proativas para manter a confiabilidade e a segurança de seus sistemas de armazenamento. É uma ferramenta valiosa para manutenção preventiva e monitoramento de discos em sistemas Linux.

# ## 1. Como verificar o HD/SSD com o Badblocks no Linux Ubuntu [1]
# 
# Para configurar o Hard Disk Manager, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Certifique-se de que seu sistema esteja atualizado.
# 
#     2.1 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update -y`
# 
#     2.2 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.3 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update -y`. Digite o seguinte comando e pressione `Enter`: `sudo apt upgrade -y`
# 
# 3. Para consultar o nome do HD e SSD no Linux Ubuntu, você pode usar os comandos `lsblk` e `fdisk`.
# 
# 3.1 **Usando `lsblk`:** O comando lsblk lista todos os dispositivos de bloco (como discos e partições) no sistema. Execute o seguinte comando no terminal: `lsblk -o NAME,SIZE,TYPE,MODEL`
# 
# Explicação:
# 
# - **`NAME`:** Mostra o nome do dispositivo.
# 
# - **`SIZE`:** Mostra o tamanho do dispositivo.
# 
# - **`TYPE`:** Mostra o tipo do dispositivo (como 'disk' para discos ou 'part' para partições).
# 
# - **`MODEL`:** Mostra o modelo do dispositivo, o que pode ajudar a identificar o HD ou SSD.
# 
# 3.2 **Usando `fdisk`:** O comando fdisk também pode ser usado para listar os discos no sistema. Execute o seguinte comando no terminal: `sudo fdisk -l`
# 
# - Este comando irá listar todos os discos e suas respectivas partições. Procure por entradas como /dev/sda ou /dev/nvme0n1 para identificar seus discos.
# 
# Ao usar esses comandos, você poderá identificar seus dispositivos pelo nome, tamanho e, no caso do `lsblk`, pelo modelo do dispositivo. Isso deve ajudá-lo a distinguir entre HD e SSD. Se o seu SSD for NVMe, o nome geralmente começará com nvme. Por outro lado, discos SATA (tanto HDs quanto SSDs) geralmente começam com sd seguido de uma letra (como sda, sdb, etc.).
# 
# 4. Para identificar bad blocks (setores defeituosos) em discos no Linux, uma ferramenta comum e robusta é o `badblocks`. Esta ferramenta faz parte do pacote `e2fsprogs`, que geralmente já está instalado na maioria das distribuições Linux, incluindo o Ubuntu.
# 
# 4.1 Veja como usar o `badblocks`:
# 
# 4.1.1 Executando `badblocks`:
# 
# a) Para verificar bad blocks em um dispositivo, execute o seguinte comando: `sudo badblocks -v /dev/sdX`
# 
# No comando acima, substitua `/dev/sdX` pelo nome do dispositivo que você deseja verificar (por exemplo, `/dev/sdb`).
# 
# Explicação:
# 
# - **v:** Modo verboso. Mostra o progresso da verificação.
# Executando badblocks com escrita e leitura:
# 
# b) Se você também desejar realizar um teste de escrita (o que destruirá todos os dados no disco), pode usar: `sudo badblocks -wv /dev/sdb`
# 
# **Atenção:** A opção `-w` é destrutiva e irá apagar todos os dados no disco. Certifique-se de ter feito backup de todos os dados importantes antes de usar esta opção.
# 
# Outras opções:
# 
# O `badblocks` tem muitas outras opções. Você pode visualizá-las consultando o manual com o comando: `man badblocks`

# ## 2. Como clonar o HD/SSD com o Data Duplicator no Linux Ubuntu [1]
# 
# No `Linux Ubuntu`, uma ferramenta popular e confiável para clonar um HD para SSD é o `dd`.
# No entanto, é crucial ter cuidado ao usar esta ferramenta porque um uso incorreto pode resultar em perda de dados.
# 
# Aqui está um exemplo de como você pode clonar um HD para SSD usando o `dd`:
# 
# 1. Identifique o nome do dispositivo do seu HD e SSD com o comando `lsblk` ou `fdisk -l`.
# 
# 2. Supondo que o seu HD seja `/dev/sda` e o SSD seja `/dev/sdb`, você pode clonar o HD para o SSD com o seguinte comando: `sudo dd if=/dev/sda of=/dev/sdb bs=64K conv=noerror,sync status=progress`
# 
# Explicação do comando:
# 
# - **if=/dev/sda:** especifica o disco de origem.
# 
# - **of=/dev/sdb:** especifica o disco de destino.
# 
# - **bs=64K:** define o tamanho do bloco para 64 kilobytes. Isso pode melhorar a velocidade de clonagem.
# 
# - **conv=noerror,sync:** permite que o `dd` continue copiando mesmo após encontrar erros e sincroniza os blocos de entrada e saída.
# 
# - **status=progress:** mostra o progresso da clonagem.
# 
# **Nota:** Antes de executar este comando, tenha certeza de que os nomes dos dispositivos estão corretos. Clonar o dispositivo errado pode resultar em perda de dados.
# 
# Outras opções para clonagem incluem ferramentas com interfaces gráficas como o "Gnome Disks" ou softwares mais avançados como o "Clonezilla". Escolha a ferramenta que você achar mais conveniente para o seu caso.

# ## 3. Como monitorar o HD/SSD com o `smartmontools` no `Linux Ubuntu` [1]
# 
# Além do `badblocks`, é uma boa prática também usar a ferramenta `smartmontools` para monitorar a saúde do disco, pois ela pode fornecer informações detalhadas sobre a condição do seu disco rígido ou SSD, incluindo setores re-alocados, contagens de erros e muito mais.
# 
# 1. Para instalar o `smartmontools` no `Ubuntu`, use: `sudo apt-get install smartmontools`
# 
# 2. E, para verificar a saúde do disco: `sudo smartctl -a /dev/sdX`
# 
#     Substitua `/dev/sdX` pelo nome do seu dispositivo.
# 
# Estas ferramentas, em conjunto, podem fornecer uma visão abrangente sobre a saúde e a condição do seu disco.

# ## Referências
# 
# [1] OPENAI. ***Clonagem hd para ssd.*** Disponível em: <https://chat.openai.com/c/2d8432ec-5047-408f-8a8e-8a7d110d72e2> (texto adaptado). Acessado em: 12/10/2023 13:31.
# 
# [2] OPEN AI. ***VS code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 16/11/2023 13:38.
# 
