# ------------------------------------------------------------------------------------
#                                    CLOUDFLARED
# ------------------------------------------------------------------------------------
# 1. Windows
WIN_CLOUDFLARED_INSTALL = "winget install --id Cloudflare.cloudflared"

# 2. Linux
LINUX_CLOUDFLARED_INSTALL = """
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64
chmod +x cloudflared-linux-amd64
sudo mv cloudflared-linux-amd64 /usr/local/bin/cloudflared
"""

# 3. MacOS
MACOS_CLOUDFLARED_INSTALL = "brew install cloudflared"


# ------------------------------------------------------------------------------------
#                                       NGROK
# ------------------------------------------------------------------------------------
# 1. Windows
WIN_NGROK_INSTALL = "winget install ngrok -s msstore"

# 2. Linux
LINUX_NGROK_INSTALL = "curl -sSL https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
  | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null \
  && echo \"deb https://ngrok-agent.s3.amazonaws.com bookworm main\" \
  | sudo tee /etc/apt/sources.list.d/ngrok.list \
  && sudo apt update \
  && sudo apt install ngrok"

# 3. MacOS
MACOS_NGROK_INSTALL = "brew install ngrok"
