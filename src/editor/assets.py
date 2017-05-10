import pygame, os

PORT_IN = pygame.image.load(os.path.join("res", "port_in.png"))
PORT_OUT = pygame.image.load(os.path.join("res", "port_out.png"))

PORT_AND2 = pygame.image.load(os.path.join("res", "port_and2.png"))
PORT_NAND2 = pygame.image.load(os.path.join("res", "port_nand2.png"))
PORT_NOR2 = pygame.image.load(os.path.join("res", "port_nor2.png"))
PORT_NOT = pygame.image.load(os.path.join("res", "port_not.png"))
PORT_OR2 = pygame.image.load(os.path.join("res", "port_or2.png"))
PORT_XOR2 = pygame.image.load(os.path.join("res", "port_xor2.png"))
PORT_XNOR2 = pygame.image.load(os.path.join("res", "port_xnor2.png"))

DOT_PATTERN = pygame.image.load(os.path.join("res", "dot_pattern.jpg"))

Assets = {
    "in": PORT_IN,
    "out": PORT_OUT,
    "and2": PORT_AND2,
    "nand2": PORT_NAND2,
    "nor2": PORT_NOR2,
    "not": PORT_NOT,
    "or2": PORT_OR2,
    "xor2": PORT_XOR2,
    "xnor2": PORT_XNOR2,
    "dot_pattern": DOT_PATTERN
}