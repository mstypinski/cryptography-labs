from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dh

DH_PUBKEY_FILENAME = ""
DH_PARAMS_FILENAME = ""


def dh_params_from_public_pem(pub_pem: bytes) -> bytes:
    # Load the public key
    public_key = serialization.load_pem_public_key(pub_pem)

    if not isinstance(public_key, dh.DHPublicKey):
        raise TypeError("Provided key is not a DH public key")

    # Extract parameters object
    params = public_key.parameters()

    # Serialize as DH PARAMETERS PEM
    pem_params = params.parameter_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.ParameterFormat.PKCS3,
    )
    return pem_params

if __name__ == "__main__":
    # Example: read DH public key from file and write DH params
    with open(DH_PUBKEY_FILENAME, "rb") as f:
        pub_pem = f.read()

    dhparam_pem = dh_params_from_public_pem(pub_pem)

    with open(DH_PARAMS_FILENAME, "wb") as f:
        f.write(dhparam_pem)

    print(f"Written DH parameters to {DH_PUBKEY_FILENAME}")
