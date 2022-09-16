# Shape Stacker v4
## [MCEdit 1.0](https://github.com/Podshot/MCEdit-Unified) filter for stacking up high end Minecraft 1.8 - 1.12.2 farms

Originally I had idea for this tool to make an [enderman farm](https://youtu.be/IKguVfcysfw), so I asked [JeWe](https://github.com/JeWe37) to make it. Later we got more ideas how to enrich it, so [Robi](https://github.com/Robitobi01) made a second version. And now I'm making third (fourth) version with even more automation.

**Old versions:**  
[Shape_Stacker_v1](https://pastebin.com/rFKW5HrJ)  
[Shape_Stacker_v2](https://pastebin.com/a94E0XfC)  
[Shape_Stacker_v3](https://www.mediafire.com/file/cnedacw6h72c0p0/Shape_Stacker_v3.py/file)  

![2022-09-16_12 00 33](https://user-images.githubusercontent.com/103208695/190599996-bfbc75c6-efc5-4edb-ac83-22d4c782a912.png)

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
1. Build a single module of your farm and place orange wool under/above where all your spawning spaces are. You can delete them later.  
![2022-09-16_12 08 10](https://user-images.githubusercontent.com/103208695/190601549-36a66a53-0fc4-4e0f-b8e9-72e615ce5a8d.png)

2. After box selecing your module in MCEdit and going into filter menu you can start tweaking options. First one is shape, as you can guess for most mob farms you will need **Cylinder** and for passive mob farms you would want **Rectangular cuboid**
![image](https://user-images.githubusercontent.com/103208695/190603515-4db234be-798c-45c2-830f-037da0cc5dbf.png)

3. Now obviusly we can select where to stack farm up (make sure original module not in the area) and radius. Important note: it's outer radius, meaning modules will not extrude from input radius, so when stacking full despawn sphere farm instead of writing 128, input 128 + module length, for example 140.  
![image](https://user-images.githubusercontent.com/103208695/190603993-495b02a8-c513-4eb8-ae55-56158af2c1d6.png)  

![2022-09-16_12 24 32](https://user-images.githubusercontent.com/103208695/190604922-2c19068c-713b-4136-a28e-356d0de594cf.png)

4. Now additional options. **Mark Center Point** will mark center with red wool.  
![2022-09-16_12 34 23](https://user-images.githubusercontent.com/103208695/190606930-a45f316f-7364-4feb-87a9-8918c0648a61.png)

5. 
![2022-09-16_12 38 25](https://user-images.githubusercontent.com/103208695/190607698-f7b95b83-a1bd-4064-a892-742d7fa2591d.png)
