# Shape Stacker v4
## [MCEdit 1.0](https://github.com/Podshot/MCEdit-Unified) filter for stacking up high end Minecraft 1.8 - 1.12.2 farms

Originally I had idea for this tool while making an [enderman farm](https://youtu.be/IKguVfcysfw), so I asked [JeWe](https://github.com/JeWe37) to make it. Later we got more ideas how to enrich it, so [Robi](https://github.com/Robitobi01) made a second version. And now I'm making third (fourth) version with even more capabilities.

**Old versions:**  
[Shape_Stacker_v1](https://pastebin.com/rFKW5HrJ)  
[Shape_Stacker_v2](https://pastebin.com/a94E0XfC)  
[Shape_Stacker_v3](https://www.mediafire.com/file/cnedacw6h72c0p0/Shape_Stacker_v3.py/file)  

![2022-09-16_12 00 33](https://user-images.githubusercontent.com/103208695/190599996-bfbc75c6-efc5-4edb-ac83-22d4c782a912.png)

Video explanation how to use **Shape Stacker v3** [here](https://youtu.be/uJSre9uzo-E), I also share a lot of useful tricks in there.

## How to install
1. Download [MCEdit-Unified](http://podshot.github.io/MCEdit-Unified/) and open mcedit.exe
2. **Quick Load** -> Select needed world -> Select an area -> Press **Filter** option in the bottom menu  
![image](https://user-images.githubusercontent.com/103208695/190597999-475972f7-1f29-4544-90bf-3a486e5571a1.png)

3. In Filter window press **Filter:**, it's a shortcut to open filter folder  
![image](https://user-images.githubusercontent.com/103208695/190598352-38073397-3c03-4b17-8369-2e36028528a5.png)

4. Download Shape_Stacker_v4.py from this repository and drag & drop it into opened filter folder  
![image](https://user-images.githubusercontent.com/103208695/190598738-68d67ca8-09b7-4407-bcb4-2947a1326c12.png)

5. Now reload filters by selectind different tool in tool box and going back to **Filter**, now you can find Shape_Stacker_v4 filter!  
![image](https://user-images.githubusercontent.com/103208695/190599111-680e2c88-40b3-480b-b443-8e2f1f9679a3.png)

## How to use
1. Build a single module of your farm and place orange wool under/above where all your spawning spaces are. You can delete it later.  
![2022-09-16_12 08 10](https://user-images.githubusercontent.com/103208695/190601549-36a66a53-0fc4-4e0f-b8e9-72e615ce5a8d.png)

2. After box selecting your module in MCEdit and going into filter menu you can start tweaking options. First one is shape, as you can guess for most mob farms you will need **Cylinder** and for passive mob farms you would want **Rectangular cuboid**
![image](https://user-images.githubusercontent.com/103208695/190603515-4db234be-798c-45c2-830f-037da0cc5dbf.png)

3. Now obviusly we can select where to stack farm up (make sure original module not in the area) and radius. Important note: it's outer radius, meaning modules will not extrude from input radius, so when stacking full despawn sphere farm instead of writing 128, input 128 + module length, for example 140.  
![image](https://user-images.githubusercontent.com/103208695/190603993-495b02a8-c513-4eb8-ae55-56158af2c1d6.png)  

![2022-09-16_12 24 32](https://user-images.githubusercontent.com/103208695/190604922-2c19068c-713b-4136-a28e-356d0de594cf.png)

4. Now additional options. **Mark Center Point** will mark center with red wool.  
![2022-09-16_12 34 23](https://user-images.githubusercontent.com/103208695/190606930-a45f316f-7364-4feb-87a9-8918c0648a61.png)

5. **Min Roof** will put just enough blocks so each spawning space has light level 0 (as we know each light level decreases spawning chances by 6.67%). Meanwhile **Extended roof** will put 41x41 roof around all spawning spaces to catch all possible packs.  
![2022-09-16_12 38 25](https://user-images.githubusercontent.com/103208695/190607698-f7b95b83-a1bd-4064-a892-742d7fa2591d.png)

6. **Set Desert** will set biome to desert 20 blocks out from all spawning spaces. If you need other biome you can use inbuilt SetBiome filter or edit Shape_Stacker_v4 code on line 70 and change biome ID to [needed biome](https://minecraft.fandom.com/wiki/Biome/IDs_before_1.13).

```py
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
```

7. Don't forget to remove orange wool after all those steps and watch [this](https://youtu.be/uJSre9uzo-E) video for more information.

## License
This program is licensed under the MIT License. Please read the License file to know about the usage terms and conditions.
