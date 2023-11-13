import ansys

def solve(population, task):
    for vector in population:
        macros = f'''
        finish
        /clear nostart
        /prep7
        resu, {task.model_file}, db
        
        sectype, 1, beam, csolid
        secdata, {vector.variables[0]}
        
        sectype, 2, beam, csolid
        secdata, {vector.variables[1]}
        /SHRINK,0   
        /ESHAPE,1.0 
        /EFACET,1   
        /RATIO,1,1,1
        /CFORMAT,32,0   
        /REPLOT 
        /solu
        solve
        
        /post1
        *get, s_max, secr, , s, eqv,max
        
        /OUT,D:\Optimizadnitsa\Workdir\Results,txt

        /com,smax = %s_max%

        /nopr
        /output
        '''

        file = open(task.work_dir + '\opt_mod.mac','w')
        file.write(macros)
        file.close()

        ansys.run('opt_mod.mac',task.work_dir)

        file = open(task.work_dir + r'\Results.txt', 'r')
        #file = open('D:Optimizadnitsa\Results.txt', 'r')
        st = file.read()
        file.close()

        smax = float(st.split(' ')[3])
        vector.stress = smax