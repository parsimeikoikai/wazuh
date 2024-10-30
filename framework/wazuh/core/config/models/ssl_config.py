from pydantic import BaseModel, FilePath
from typing import Literal


class SSLConfig(BaseModel):
    key: FilePath = "var/ossec/etc/etc/sslmanager.key"
    cert: FilePath = "var/ossec/etc/sslmanager.cert"
    ca: FilePath = "var/ossec/etc/sslmanager.ca"
    keyfile_password: str = ""


class ManagementAPISSLConfig(BaseModel):
    key: str = "server.key"
    cert: str = "server.crt"
    use_ca: bool = False
    ssl_protocol: Literal["TLS", "TLSv1", "TLSv1.1", "TLSv1.2", "auto"] = "auto"
    ssl_ciphers: str = ''

