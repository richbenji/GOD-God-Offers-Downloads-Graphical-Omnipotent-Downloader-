# 🎓 Tutorial — GOD (God Offers Downloads)

## 🚀 Apresentação
Bem-vindo ao guia de utilização da aplicação! Esta aplicação permite descarregar vídeos e playlists do YouTube em formato de vídeo ou áudio, com suporte para playlists privadas.

A aplicação oferece dois modos principais:

- 🔥 **Descarregamento simples**: para gerir vídeos um a um (ou playlists)
- 📋 **Descarregamento em lote (Batch)**: para descarregar vários URLs de uma só vez

------

## 🔥 Descarregamento simples

1. **Copie o URL** do vídeo do YouTube 🔗

2. **Cole-o** no campo de URL

3. **Clique** no botão "➕ Verificar"

4. **Aguarde** que as informações do vídeo sejam carregadas (miniatura, duração, tamanho)

   **Selecione** as suas opções:

   - 🎥 **Vídeo**: escolha a resolução (Best, 2160p, 1440p, 1080p, 720p, 480p, 360p, 240p, 144p)
   - 🎵 **Apenas áudio**: escolha o bitrate (Best, 320, 256, 192, 128, 96, 64, 32 kbps) e o formato (M4A ou MP3)

   **Clique** em "⬇️ Descarregar"

   **Selecione** a pasta de destino

### Dicas 💡

- Pode **adicionar vários vídeos** à fila de espera antes de iniciar o descarregamento
- O **tamanho total** e o número de vídeos são exibidos no botão de descarregamento
- Use o botão **🗑️ Esvaziar a fila** para apagar todos os vídeos em espera
- Clique no botão **ℹ️** ao lado de cada vídeo para ver informações detalhadas (formatos disponíveis, descrição, etc.)
- Clique em **❌** para remover um vídeo da fila de espera

------

## 📚 Playlists

### Playlists públicas

Simplesmente copie o URL da playlist no separador "Descarregamento único", a aplicação detetará automaticamente todos os vídeos! Pode modificar as opções de vídeo/áudio antes de iniciar o descarregamento.

A aplicação:

- ✅ Carrega automaticamente todos os vídeos da playlist
- ✅ Exibe uma miniatura e informações para cada vídeo
- ✅ Permite personalizar as opções para cada vídeo individualmente
- ✅ Descarrega tudo numa única operação

### 🪪 Playlists privadas
#### Método 1: Ligação automática via navegador (Recomendado ⭐)

**A aplicação usa automaticamente os seus cookies do Firefox se estiver ligado ao YouTube!**

1. **Inicie sessão** na sua conta do YouTube no Firefox
2. **Copie** o URL da sua playlist privada
3. **Cole-o** na aplicação
4. ✅ **Funciona automaticamente!** A aplicação acede aos seus cookies do Firefox

> 💡 **Dica**: Permaneça ligado ao YouTube no Firefox para que a aplicação possa sempre aceder às suas playlists privadas sem manipulação adicional.

#### Método 2: Exportação manual de cookies (Alternativa)

Se o método automático não funcionar ou se usar outro navegador, deve fornecer os seus **cookies do YouTube**:

1. Instale uma extensão do navegador:
   - **Firefox**: [cookies.txt](https://addons.mozilla.org/pt-PT/firefox/addon/cookies-txt/) ou [get cookies](https://addons.mozilla.org/pt-PT/firefox/addon/get_cookies/)
   - **Chrome**: [Get cookies.txt LOCALLY](https://chrome.google.com/webstore)

2. Inicie sessão no YouTube
3. **Exporte** os seus cookies no formato Netscape (ficheiro `.txt`)
4. **Clique** no botão "🪪 ⬆️ cookies.txt" no canto superior esquerdo da aplicação
5. **Selecione** o seu ficheiro `cookies.txt`
6. **Teste** com a sua playlist privada

> ⚠️ **Atenção**: Nunca partilhe o seu ficheiro cookies.txt, ele contém as suas credenciais de início de sessão!

### ⚠️ Conselhos
- Não elimine o ficheiro cookies.txt
- Se aparecer um erro, recarregue os cookies

------

## 📦 Descarregamento em lote (Batch)

O separador "Descarregamento em lote" permite descarregar vários vídeos com as **mesmas definições** para todos.

### Utilização

1. **Abra** o separador "Descarregamento em lote"
2. **Introduza** os URLs dos vídeos (um por linha) na área de texto
   - OU clique em "⬆️ Carregar de um ficheiro" para importar um ficheiro `.txt` contendo os seus URLs
3. **Selecione** o tipo:
   - 🎥 **Vídeo**: com resolução comum para todos
   - 🎵 **Apenas áudio**: com bitrate comum para todos
4. **Escolha** a resolução (se vídeo) e o bitrate de áudio
5. **Clique** em "⬇️ Descarregar"
6. **Selecione** a pasta de destino

### Diferença em relação ao descarregamento simples

| Descarregamento simples | Descarregamento em lote |
| --- | --- |
| Opções **personalizadas** por vídeo | Opções **idênticas** para todos |
| Exibe miniaturas e informações detalhadas | Interface simplificada |
| Ideal para alguns vídeos variados | Ideal para muitos vídeos semelhantes |

------

## ⚙️ Opções avançadas

### Resolução de vídeo

| Resolução | Uso recomendado | Tamanho aproximado (1h) |
| --- | --- | --- |
| **Best** | Melhor qualidade disponível | Variável |
| **2160p (4K)** | Ecrãs 4K, arquivo | ~4-8 GB |
| **1440p (2K)** | Monitores de alta definição | ~2-4 GB |
| **1080p (Full HD)** | Uso padrão, melhor compromisso ⭐ | ~1-2 GB |
| **720p (HD)** | Dispositivos móveis, economia de espaço | ~500 MB-1 GB |
| **480p** | Ligação lenta, armazenamento limitado | ~300-500 MB |
| **360p** | Ligação muito lenta | ~200-300 MB |

> 💡 **Conselho**: Para uso quotidiano, **1080p** oferece o melhor compromisso qualidade/tamanho.

### Bitrate de áudio

| Bitrate | Qualidade | Uso recomendado | Tamanho (1h) |
| --- | --- | --- | --- |
| **Best** | Máximo disponível | Arquivo, audiófilos ⭐ | Variável |
| **320 kbps** | Excelente | Música de alta qualidade | ~140 MB |
| **256 kbps** | Muito boa | Uso padrão | ~115 MB |
| **192 kbps** | Boa | Compromisso qualidade/tamanho | ~85 MB |
| **128 kbps** | Aceitável | Podcasts, conferências | ~60 MB |
| **96 kbps** | Razoável | Apenas voz | ~45 MB |
| **64 kbps** | Fraca | Ligação muito lenta | ~30 MB |

### Formato de áudio

- **M4A**:
  - ✅ Melhor qualidade com tamanho igual
  - ✅ Ficheiros mais leves
  - ✅ Formato nativo do YouTube (sem conversão)
  - ❌ Menos compatível com leitores antigos
- **MP3**:
  - ✅ Compatível com todos os dispositivos
  - ✅ Amplamente suportado
  - ✅ Personalizável (bitrate à escolha)
  - ❌ Requer conversão (FFmpeg necessário)

------

## Personalização

### 🌍 Mudar o idioma

Clique no seletor de idioma 🌍 no canto superior esquerdo para escolher entre os idiomas disponíveis.

### 🌓 Modo escuro / claro

Use o interruptor **🌙 / ☀️** para alternar entre os temas.

------

## ❓ Problemas frequentes

### "The playlist does not exist"

**Causas possíveis:**

1. A playlist é **privada** → Certifique-se de que está ligado ao YouTube no Firefox, ou forneça um ficheiro `cookies.txt`
2. O URL está incorreto → Verifique se copiou o URL completo da playlist
3. A playlist foi eliminada → Verifique se ainda existe no YouTube

### "ERROR: unable to download video data"

**Causas possíveis:**

1. Ligação à internet instável
2. Vídeo eliminado ou privado
3. O YouTube mudou o seu formato → Atualize o yt-dlp: `pip install -U yt-dlp`

### Descarregamento lento

- **Soluções:**
  - ✅ Verifique a sua ligação à internet 📶
  - ✅ O YouTube por vezes limita a velocidade conforme a sua localização
  - ✅ Tente descarregar noutro momento
  - ✅ Descarregue com uma resolução mais baixa (720p em vez de 1080p)

### Erro de conversão MP3

**Erro**: `ERROR: ffmpeg not found`

**Solução**: A conversão para MP3 requer o **FFmpeg** instalado no seu sistema.

**Instalação do FFmpeg:**

```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# Fedora
sudo dnf install ffmpeg

# Arch Linux
sudo pacman -S ffmpeg

# macOS (Homebrew)
brew install ffmpeg

# Windows (Chocolatey)
choco install ffmpeg
```

**Verificar a instalação:**

```bash
ffmpeg -version
```

### O descarregamento pára nos 99%

Isto é normal! A aplicação está a **fundir** o vídeo e o áudio (ou a converter para MP3). Esta etapa pode demorar alguns segundos a alguns minutos dependendo de:

- O tamanho do ficheiro
- A potência do seu computador
- A resolução escolhida

> 💡 **Dica**: Não feche a aplicação enquanto a barra de progresso estiver nos 99%!

### "Permission denied" durante o descarregamento

**Causas possíveis:**

1. A pasta de destino está protegida contra escrita
2. Um ficheiro com o mesmo nome já está aberto
3. O seu antivírus está a bloquear a escrita

**Soluções:**

- ✅ Escolha uma pasta no seu diretório pessoal (Documentos, Transferências)
- ✅ Feche qualquer ficheiro de vídeo aberto
- ✅ Adicione uma exceção no seu antivírus

## 📞 Suporte

### Obter ajuda

Para qualquer questão ou problema:

- 🐛 Relate um bug no [GitHub](https://github.com/richbenji/Ultimate-GUI-YouTube-Downloader-yt-dlp-Ctk)

- 💬 **Questão**: Consulte primeiro este tutorial, depois abra uma issue no GitHub

- ⭐ **Gosta da aplicação?**: Dê uma estrela no GitHub!

### Contribuir

O projeto é open-source! As contribuições são bem-vindas:

- 🔧 Correções de bugs
- ✨ Novas funcionalidades
- 🌍 Traduções adicionais
- 📖 Melhoria da documentação

------

## 📜 Menções legais

### Uso responsável

Esta aplicação é uma ferramenta de descarregamento. **Você é responsável** pelo uso que faz dela:

- ✅ **Autorizado**: Descarregar os seus próprios vídeos, conteúdo sob licença livre, ou conteúdo para o qual tem autorização
- ❌ **Proibido**: Descarregar conteúdo protegido por direitos de autor sem permissão, redistribuir conteúdo descarregado

> ⚠️ **Importante**: Respeite sempre os termos de utilização do YouTube e as leis de direitos de autor do seu país.

------

**Bom descarregamento! 🎉**