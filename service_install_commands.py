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

