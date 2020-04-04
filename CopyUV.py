import pymel.core as pm
import sys


def CopyUV():
    """

    Returns: Copy UV form two object even one have skin weight

    """
    selection = pm.ls(sl=True)
    history = pm.listHistory(selection[1])
    list_his = pm.ls(history , type='skinCluster')
    if len(list_his) != 0:
        child = pm.listRelatives(selection[1])
        for c in child:
            if 'Orig' in str(c):
                pm.setAttr('{}.intermediateObject'.format(c) , 0)
                pm.transferAttributes(selection[0] , c , transferPositions=0 , transferNormals=0 , transferUVs=2 ,
                                      transferColors=2 , sampleSpace=4 , sourceUvSpace='map1' , flipUVs=0)
                pm.delete(c , ch=True)
                pm.setAttr('{}.intermediateObject'.format(c) , 1)
                sys.stdout.write('Copy UV is done\n')
            else:
                pass
    else:
        pm.transferAttributes(selection[0] , selection[1] , transferPositions=0 , transferNormals=0 , transferUVs=2 ,
                              transferColors=2 , sampleSpace=4 , sourceUvSpace='map1' , flipUVs=0)
        pm.delete(selection[1] , ch=True)
        sys.stdout.write('Copy UV is done\n')
