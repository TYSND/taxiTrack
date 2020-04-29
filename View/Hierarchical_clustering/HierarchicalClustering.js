/**
 * HierarchicalCClustering.js by lpjworkroom
 *
 */

class HierarchicalClustering{
    /*
    * node:{
    *   type:"node"|"leaf",
    *   id:number,  //index in tree array
    *   left:,right:number, //if type=="node"
    *   lon:,lat:number, //if type=="leaf"
    * }
    * tree:[] of node
    */
    var tree=[];
    constructor(treeArr){
        this.tree=treeArr;
    }

    /*para:
    *   dep:number, //selected depth of node in tree
    */
    function clusteringByDepth(dep){
        let clusters=new GetNodeByDepth(tree,dep);
        let colors=getClusterColors(clusters.length);
        clusters=getPOIOfClusters(clusters);
        drawClusters(clusters,colors);
    }
}


/*return nodes in tree of given depth
* */
class GetNodeByDepth{
    constructor(tree,dep){
        function dfs({now,nowDep,target,ret}){
            if (now===null)  return;
            if (nowDep==target){
                ret.push(now);
                return;
            }
            dfs({now.left,nowDep+1,target,ret});
            dfs({now.right,nowDep+1,target,ret});
        }

        let ret=[];
        dfs({
            now:tree[0],
            nowDep:0,
            target:dep,
            ret:ret,
        });
        return ret;
    }
}


/*return high contrast colors of given amount
* */
function getClusterColors(num){
    var ret=[];
    return ret;
}


/*given clusters' roots,return all POIs divided in these clusters
* */
class getPOIOfClusters(){
    constructor(clusters){
        var ret=[];
        for (let root of clusters)
            ret.push(getAllLeaf(root));
        return ret;
    }

    function getAllLeaf(root){
        function dfs(now,ret){
            if (now===null) return;
            if (now.left===null&&now.right===null)
                ret.push(now);
            dfs(now.left,ret);
            dfs(now.right,ret);
        }

        var ret=[];
        dfs(root,ret);
        return ret;
    }
}

