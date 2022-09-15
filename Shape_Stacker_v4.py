# Shape Stacker v4 by KK / Robi / JeWe
# MIT License Copyright (c) 2022 KK / Robi / JeWe v4
# First version was made by JeWe and updated by Robi
# KK: https://www.youtube.com/c/kkochanovskii
# Robi: https://www.youtube.com/user/robitobi01
# JeWe: https://www.youtube.com/channel/UCcxdJHlnP-z8NceLyxQnzRA

from math import hypot

inputs = (
    ("Shape Stacker by KK | Robi | JeWe", "label"),
    ("", "label"),
    ("Shape", ("Cylinder", "Rectangular cuboid")),
    ("", "label"),
    ("Center", "label"),
    ("X", 0),
    ("Y", 0),
    ("Z", 0),
    ("Radius", 128),
    ("","label"),
    ("Options:", "label"),
    ("Mark Center Point", True),
    ("Min Roof", False),
    ("Extended Roof", False),
    ("Set Desert", False),
)

def copyFromBox(level, x1, y1, z1, options):
    global bx
    for x in xrange(bx.minx, bx.maxx):
        for y in xrange(bx.miny, bx.maxy):
            for z in xrange(bx.minz, bx.maxz):
                level.setBlockAt(x1 + x - bx.minx, y1 + y - bx.miny, z1 + z - bx.minz, level.blockAt(x, y, z))
                level.setBlockDataAt(x1 + x - bx.minx, y1 + y - bx.miny, z1 + z - bx.minz, level.blockDataAt(x, y, z))
                if level.blockAt(x1 + x - bx.minx, y1 + y - bx.miny, z1 + z - bx.minz) == 35 and \
                   level.blockDataAt(x1 + x - bx.minx, y1 + y - bx.miny, z1 + z - bx.minz) == 1:
                    # Places minimal roof for light level 0 at all orangle wool blocks
                    if options["Min Roof"]:
                        buildMinRoof(level, x1 + x - bx.minx, y1 + bx.maxy - bx.miny - 1, z1 + z - bx.minz)
                        
                    # Places 41x41 roof around all orangle wool blocks (catches all spawning attempts)
                    if options["Extended Roof"]:
                        buildMaxRoof(level, x1 + x - bx.minx, y1 + bx.maxy - bx.miny - 1, z1 + z - bx.minz)
                     
                    # Sets biome to desert        
                    if options["Set Desert"]:                   
                        setDesert(level, x1 + x - bx.minx, z1 + z - bx.minz)
                
def buildMinRoof(level, x0, y0, z0):
    for x in xrange(-14, 15):
        for z in xrange(-14, 15):
            if abs(x) + abs(z) <= 14 and (level.blockAt(x0 + x, y0, z0 + z) == 0 or level.blockAt(x0 + x, y0, z0 + z) == 126):
                level.setBlockAt(x0 + x, y0, z0 + z, 126)
                level.setBlockDataAt(x0 + x, y0, z0 + z, 5)             
    level.setBlockAt(x0, y0, z0, 44)
    level.setBlockDataAt(x0, y0, z0, 3)
    
def buildMaxRoof(level, x0, y0, z0):
    for x in xrange(-20, 21):
        for z in xrange(-20, 21):
            if level.blockAt(x0 + x, y0, z0 + z) == 0:
                level.setBlockAt(x0 + x, y0, z0 + z, 126)
                level.setBlockDataAt(x0 + x, y0, z0 + z, 1)             
    level.setBlockAt(x0, y0, z0, 44)
    level.setBlockDataAt(x0, y0, z0, 3)
  
def setDesert(level, x0, z0):
    # Code taken from SethBling's setbiome filter http://youtube.com/SethBling
    # Desert ID is - 2
    biome = 2
    minx = x0 - 20
    maxx = x0 + 21
    minz = z0 - 20
    maxz = z0 + 21
    minxC = int(minx / 16) * 16
    minzC = int(minz / 16) * 16
    for x in xrange(minxC, maxx, 16):
        for z in xrange(minzC, maxz, 16):
            chunk = level.getChunk(x / 16, z / 16)
            chunk.dirty = True
            array = chunk.root_tag["Level"]["Biomes"].value
            chunkx = int(x / 16) * 16
            chunkz = int(z / 16) * 16
            for bx in xrange(max(minx, chunkx), min(maxx, chunkx + 16)):
                for bz in xrange(max(minz, chunkz), min(maxz, chunkz + 16)):
                    idx = 16 * (bz - chunkz) + (bx - chunkx)
                    array[idx] = biome
            chunk.root_tag["Level"]["Biomes"].value = array                  

def perform(level, box, options):
    global bx
    bx = box
    r = options["Radius"]
    x0, y0, z0 = options["X"], options["Y"], options["Z"]
    bxDX, bxDZ = bx.maxx - bx.minx, bx.maxz - bx.minz

    if options["Shape"] == "Cylinder":
        for x in xrange(x0, x0 - r, -bxDX):
            for z in xrange(z0, z0 - r, -bxDZ):
                 if hypot(x - x0, z - z0) < r and \
                    hypot(x - x0 + bxDX, z - z0) < r and \
                    hypot(x - x0, z - z0 + bxDZ) < r and \
                    hypot(x - x0 + bxDX, z-z0 + bxDZ) < r:
                     copyFromBox(level, x, y0, z, options)
            for z in xrange(z0, z0 + r, bxDZ):
                 if hypot(x - x0, z - z0) < r and \
                    hypot(x - x0 + bxDX, z - z0) < r and \
                    hypot(x - x0, z - z0 + bxDZ) < r and \
                    hypot(x - x0 + bxDX, z - z0 + bxDZ) < r:
                     copyFromBox(level, x, y0, z, options)
        for x in xrange(x0, x0 + r, bxDX):
            for z in xrange(z0, z0 - r, - bxDZ):
                 if hypot(x - x0, z - z0) < r and \
                    hypot(x - x0 + bxDX, z - z0) < r and \
                    hypot(x - x0, z - z0 + bxDZ) < r and \
                    hypot(x - x0 + bxDX, z - z0 + bxDZ) < r:
                     copyFromBox(level, x, y0, z, options)
            for z in xrange(z0, z0 + r, bxDZ):
                 if hypot(x - x0, z - z0) < r and \
                    hypot(x - x0 + bxDX, z - z0) < r and \
                    hypot(x - x0, z - z0 + bxDZ) < r and \
                    hypot(x - x0 + bxDX, z - z0 + bxDZ) < r:
                     copyFromBox(level, x, y0, z, options)

    if options["Shape"] == "Rectangular cuboid":
        for x in xrange(x0, x0 - r, -bxDX):
            for z in xrange(z0, z0 - r, - bxDZ):
                    copyFromBox(level, x, y0, z, options)
            for z in xrange(z0, z0 + r, bxDZ):
                    copyFromBox(level, x, y0, z, options)
        for x in xrange(x0, x0 + r, bxDX):
            for z in xrange(z0, z0 - r, - bxDZ):
                    copyFromBox(level, x, y0, z, options)
            for z in xrange(z0, z0 + r, bxDZ):
                    copyFromBox(level, x, y0, z, options)
    
    if options["Mark Center Point"]:
        for x in xrange(x0 - 1, x0 + 2):
            for y in xrange(y0 - 1, y0 + 2):
                for z in xrange(z0 - 1, z0 + 2):
                    level.setBlockAt(x, y , z, 0)
        level.setBlockAt(x0, y0, z0, 35)
        level.setBlockDataAt(x0, y0, z0, 14)
                        
    for x in xrange((x0 - r) // 16, (x0 + r) // 16):
        for z in xrange((z0 - r) // 16, (z0 + r) // 16):
            level.getChunk(x, z).dirty = True
    