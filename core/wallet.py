# import bitcoin
# import ecdsa
import os
import bitcoin
# import binascii
# from hashlib import sha256
# from ecdsa.util import string_to_number, number_to_string

class wallet(object):

  def __init__(self):
    self.public_key = ''
    self.private_key = ''

    pass

  # def base58encode(self, n):
  #   # Prepend the 0x80 version/application byte
  #   private_key = b'\x80' + n
  #   # Append the first 4 bytes of SHA256(SHA256(private_key)) as a checksum
  #   private_key += sha256(sha256(private_key).digest()).digest()[:4]
  #   # Convert to Base58 encoding
  #   code_string = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
  #   value = int.from_bytes(private_key, byteorder='big')
  #   output = ""
  #   while value:
  #     value, remainder = divmod(value, 58)
  #     output = code_string[remainder] + output
  #   return output    

  # def random_secret(self, key = os.urandom(32)):
  #   convert_to_str = lambda array: ''.join(str(byte) for byte in array)

  #   return int(convert_to_str(key), 16)

  # def get_point_pubkey(self, point):
  #   if point.y() & 1:
  #     key = '03' + '%064x' % point.x()
  #   else:
  #     key = '02' + '%064x' % point.x()

  #   return key

  # def test1(self):
  #   result = {}
  #   # secp256k1, http://www.oid-info.com/get/1.3.132.0.10
  #   _p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
  #   _r = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
  #   _b = 0x0000000000000000000000000000000000000000000000000000000000000007
  #   _a = 0x0000000000000000000000000000000000000000000000000000000000000000
  #   _Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
  #   _Gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
  #   curve_secp256k1 = ecdsa.ellipticcurve.CurveFp(_p, _a, _b)
  #   generator_secp256k1 = ecdsa.ellipticcurve.Point(curve_secp256k1, _Gx, _Gy, _r)
  #   oid_secp256k1 = (1, 3, 132, 0, 10)
  #   SECP256k1 = ecdsa.curves.Curve('SECP256k1', curve_secp256k1, generator_secp256k1, oid_secp256k1)
  #   ec_order = _r

  #   curve = curve_secp256k1
  #   generator = generator_secp256k1

  #   # Generate a new private key.
  #   secret_key = os.urandom(32)
  #   secret = self.random_secret(secret_key)

  #   result['private_key_dec'] = secret
  #   result['secret_key'] = int.from_bytes(secret_key, byteorder='big')
  #   result['secret_key_58'] = self.base58encode(secret_key)

  #   # Get the public key point.
  #   point = secret * generator
  #   result['public_key'] = str(point)

  #   # result['bitcoin_address_compressed'] = int.from_bytes(self.get_point_pubkey(point), byteorder='big')

  #   result['bitcoin_address'] = self.get_point_pubkey(point)

  #   return result


# test1() vs test()
# need to compress pub key
# {'secret_key_58': '5HwfZDuZazMEaYRQ5va85xEtpgWkncPZ54XZKMYfJtLi6paZb55', 'public_key': '(87683569545154849100949636626005868138045772194104455225660464830691777178044,89675619655127001200455492779346942960745055014995213151620690784706647509676)', 'secret_key': 7578340299196389828612605628484314963513122510741408100431794476208991022027, 'bitcoin_address': '02c1db2442b60efe9af14400d5d720f8a7043f430fe26e5e4068f51ab54783e9bc', 'private_key_dec': 193339471020636547924206028123599572328127341840628211859218753310239040869255756524643257039050969603}
# ====================================
# {'wif': '5Jf7dG4BUXYG2fyBZVKwifLrMuNPMHxpiH7aH9tTFLvbqVcmmQa', 'private_key_compressed_hex': '6edee963c06b3ef2758afb6a097b81f03e12cddbbefedbac9b367ff62e1a215901', 'bitcoin_address_compressed': '18VZZkEbdJHMgV3xg49YaV4rxD714ZM83U', 'bitcoin_address': '1M1E7ZEKhCa1H2V28xo8zV7Uhhi7WVH1MC', 'private_key_hex': '6edee963c06b3ef2758afb6a097b81f03e12cddbbefedbac9b367ff62e1a2159', 'private_key_dec': 50148264188737704690879791256601082022554188115509880710089775062875094262105, 'private_key_compressed_wif': 'KzwEF3T3EVnyLNzycQ2cWtEcsG9PeZsPbC81tJE6rJwaku5Xdas7', 'public_key': (32644585136304814356656023794024100879091245924523823688351220301803322373503, 100952066461685327111349222848377098017243902008859522582102727199939775015224), 'public_key_compressed_hex': '02482c2e2fbe01781597598515b4ecfbdadc8994d653c22630a4b1720b0984757f', 'public_key_hex': '04482c2e2fbe01781597598515b4ecfbdadc8994d653c22630a4b1720b0984757fdf30d8427160f41035c60f11a921c9ee72650752189640a38f0564119e91a938'}

# ====================================

  def get(self):
    return {
      'private_key': self.private_key,
      'wallet_address': self.wallet_address,
      'wallet_address_compressed': self.wallet_address_compressed,
      'wif_private_key_compressed': self.wif_private_key_compressed,
      'dict': self.__dict__ #temporary
    }

  def create(self):
    # Generate a random private key
    valid_private_key = False
    while not valid_private_key:
      self.private_key = bitcoin.random_key()
      self.decoded_private_key = bitcoin.decode_privkey(self.private_key, 'hex')
      valid_private_key =  0 < self.decoded_private_key < bitcoin.N

    # Convert private key to WIF format
    self.wif_encoded_private_key = bitcoin.encode_privkey(self.decoded_private_key, 'wif')

    # Add suffix "01" to indicate a compressed private key
    self.private_key_compressed = self.private_key + '01'
 
    # Generate a WIF format from the compressed private key (WIF-compressed)
    self.wif_private_key_compressed = bitcoin.encode_privkey(bitcoin.decode_privkey(self.private_key_compressed, 'hex'), 'wif')

    # Multiply the EC generator point G with the private key to get a public key point
    self.public_key = bitcoin.fast_multiply(bitcoin.G, self.decoded_private_key)

    # Encode as hex, prefix 04
    self.hex_encoded_public_key = bitcoin.encode_pubkey(self.public_key,'hex')

    # Compress public key, adjust prefix depending on whether y is even or odd
    (public_key_x, public_key_y) = self.public_key

    if (public_key_y % 2) == 0:
        compressed_prefix = '02'
    else:
        compressed_prefix = '03'

    self.hex_compressed_public_key = compressed_prefix + bitcoin.encode(public_key_x, 16)

    # Generate bitcoin address from public key
    self.wallet_address = bitcoin.pubkey_to_address(self.public_key) #"Bitcoin Address (b58check) is: %s\n" % 

    # Generate compressed bitcoin address from compressed public key
    self.wallet_address_compressed = bitcoin.pubkey_to_address(self.hex_compressed_public_key) #"Compressed Bitcoin Address (b58check) is: %s" % 

    return self

  def test(self):
    # Generate a random private key
    valid_private_key = False
    while not valid_private_key:
      private_key = bitcoin.random_key()
      decoded_private_key = bitcoin.decode_privkey(private_key, 'hex')
      valid_private_key =  0 < decoded_private_key < bitcoin.N
    result = {}
    result['private_key_hex'] = private_key #"Private Key (hex) is: %s\n" %
    result['private_key_dec'] = decoded_private_key #"Private Key (decimal) is: %s\n" % 

    # Convert private key to WIF format
    wif_encoded_private_key = bitcoin.encode_privkey(decoded_private_key, 'wif')
    result['wif'] = wif_encoded_private_key #"Private Key (WIF) is: %s\n" % 

    # Add suffix "01" to indicate a compressed private key
    compressed_private_key = private_key + '01'
    result['private_key_compressed_hex'] = compressed_private_key #"Private Key Compressed (hex) is: %s\n"

    # Generate a WIF format from the compressed private key (WIF-compressed)
    wif_compressed_private_key = bitcoin.encode_privkey(
        bitcoin.decode_privkey(compressed_private_key, 'hex'), 'wif')
    result['private_key_compressed_wif'] = wif_compressed_private_key #"Private Key (WIF-Compressed) is: %s\n" % 

    # Multiply the EC generator point G with the private key to get a public key point
    public_key = bitcoin.fast_multiply(bitcoin.G, decoded_private_key)
    result['public_key'] = public_key #"Public Key (x,y) coordinates is: (%i,%i)\n" % 

    # Encode as hex, prefix 04
    hex_encoded_public_key = bitcoin.encode_pubkey(public_key,'hex')
    result['public_key_hex'] = hex_encoded_public_key #"Public Key (hex) is: %s" % 

    # Compress public key, adjust prefix depending on whether y is even or odd
    (public_key_x, public_key_y) = public_key
    if (public_key_y % 2) == 0:
        compressed_prefix = '02'
    else:
        compressed_prefix = '03'
    hex_compressed_public_key = compressed_prefix + bitcoin.encode(public_key_x, 16)
    result['public_key_compressed_hex'] = hex_compressed_public_key #"Compressed Public Key (hex) is: %s\n" % 

    # Generate wallet address from public key
    result['wallet_address'] = bitcoin.pubkey_to_address(public_key) #"Bitcoin Address (b58check) is: %s\n" % 

    # Generate compressed bitcoin address from compressed public key
    result['wallet_address_compressed'] = bitcoin.pubkey_to_address(hex_compressed_public_key) #"Compressed Bitcoin Address (b58check) is: %s" % 
    return result

