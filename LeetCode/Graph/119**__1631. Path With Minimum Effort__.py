from typing import List, Tuple

class Solution:
    def dfs(self,row,col,mat,mid,visited):
        visited.add(str(row)+"-"+str(col))
        if row==len(mat)-1 and col==len(mat[0])-1:
            print("with jump ",mid)
            return True
        dr=[+1,-1,0,0]
        dc=[0,0,-1,+1]
        for i in range(4):
            rr=row+dr[i]
            cc=col+dc[i]
            if rr<0 or cc<0 or rr>=len(mat) or cc>=len(mat[0]):
                continue
            if str(rr)+"-"+str(cc) in visited:
                continue
            if abs(mat[row][col]-mat[rr][cc])<=mid:
                if self.dfs(rr,cc,mat,mid,visited):
                    return True
        return False
            
        
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        l=0
        r=10**9+2
        while l<r:
            mid=(l+r)//2
            print(l,r,mid)
            visited=set()
            if self.dfs(0,0,heights,mid,visited):
                r=mid
            else:
                l=mid+1
               
        return l
    
sol=Solution()
heights =[[315,310,39,569,795,396,912,460,25,656,786,57,302,82,381,181,730,288,389,364,517,601,897,853,205,300,667,802,520,59,436,201],[760,906,573,187,226,786,738,966,393,411,140,432,871,344,112,935,88,497,515,352,46,997,906,441,673,291,87,150,639,556,615,787],[137,505,508,774,253,292,432,668,130,252,184,847,640,275,539,52,492,286,718,63,342,161,524,263,176,944,576,520,162,839,960,230],[641,610,952,411,609,509,141,352,562,261,846,583,247,260,960,28,23,988,895,245,90,348,416,906,59,277,966,301,37,399,608,17],[802,309,118,177,339,613,463,532,667,121,923,364,415,841,37,927,379,378,651,697,235,751,13,883,654,341,319,550,637,683,596,113],[203,763,873,300,748,136,603,179,579,290,858,608,630,143,602,315,593,463,211,422,676,714,507,628,486,264,559,993,97,762,814,417],[339,553,186,104,493,228,801,945,674,702,630,770,380,45,799,604,205,795,884,708,771,296,91,669,130,832,322,2,816,244,263,808],[701,352,436,513,237,564,123,763,189,566,917,624,262,553,893,591,490,842,938,490,444,149,420,236,382,125,309,872,895,826,265,308],[61,305,699,235,933,342,767,175,924,937,279,802,819,697,782,373,645,578,344,814,231,325,3,853,175,684,148,794,572,349,861,547],[351,690,400,998,628,535,577,763,961,420,941,741,238,362,261,639,805,604,816,863,968,164,371,846,922,784,610,458,408,908,793,13],[458,205,776,312,823,527,38,49,687,771,827,101,413,746,51,476,270,563,439,866,892,262,449,44,395,290,64,640,892,692,225,959],[13,486,397,950,102,687,467,496,498,927,335,739,551,47,381,604,291,116,124,185,73,827,410,327,171,282,902,816,258,818,298,246],[803,461,742,261,679,732,892,874,445,121,610,664,556,738,649,693,54,900,139,280,352,279,344,537,616,429,472,227,432,545,698,654],[392,719,411,99,735,789,950,514,732,874,573,121,819,675,906,1,521,124,81,854,207,96,173,333,629,990,899,652,38,287,458,385],[361,998,49,430,434,299,896,776,911,906,905,664,302,336,454,250,396,843,125,169,871,127,11,926,182,23,245,296,173,607,680,961],[640,983,528,48,856,643,587,943,955,596,220,673,139,458,763,575,972,768,767,905,797,801,226,963,442,776,243,998,302,304,669,783],[40,94,468,810,301,226,617,941,963,62,685,220,767,850,480,253,996,706,648,194,965,612,316,193,49,570,157,949,837,755,800,826],[112,8,342,892,976,28,335,882,464,275,747,459,169,210,875,69,416,874,912,282,779,278,595,591,54,847,887,919,650,39,908,914],[810,416,508,490,643,968,658,92,302,410,416,441,250,854,394,488,853,118,881,435,809,340,864,137,766,766,227,875,723,598,193,927],[924,613,954,886,974,394,927,594,154,653,310,360,200,907,230,872,578,256,495,643,553,576,212,378,610,446,447,607,845,635,543,537],[181,758,54,222,529,182,371,601,179,263,291,739,537,130,66,529,885,474,843,330,910,325,797,168,428,338,656,819,832,384,835,82],[294,699,160,972,888,63,411,837,919,3,250,923,252,994,458,726,489,754,450,231,107,922,615,917,668,774,645,528,60,253,626,42],[982,276,303,29,850,853,242,49,530,41,896,733,5,674,936,437,266,967,955,403,868,394,498,707,876,13,34,996,467,317,77,220],[757,445,461,511,821,259,239,380,903,878,588,628,962,369,26,868,611,884,519,297,187,170,519,281,287,442,966,63,222,444,687,65],[875,386,317,164,741,846,527,681,497,235,107,238,182,894,101,94,911,861,394,42,646,791,612,515,177,334,367,981,685,175,912,633],[943,250,413,632,418,32,961,639,992,834,723,734,107,893,624,724,471,825,251,64,548,533,230,669,38,753,389,759,785,732,290,807],[584,399,638,588,571,463,795,116,388,925,654,146,513,578,240,983,594,292,859,924,679,253,360,815,4,853,543,84,167,297,356,573],[855,810,897,902,760,71,224,113,583,156,729,178,751,312,111,562,350,136,389,571,633,347,781,827,887,49,451,861,76,550,596,359],[721,788,543,254,226,694,462,647,800,737,366,161,476,808,583,669,124,593,209,806,709,507,565,230,488,983,659,1,977,507,30,497],[452,493,459,1,425,348,389,281,521,546,546,330,795,541,357,335,826,814,425,701,904,470,334,751,390,411,391,901,427,386,706,541],[997,477,430,998,14,307,829,228,325,435,980,5,1,208,277,379,667,957,271,233,126,357,131,294,408,352,897,396,256,555,329,479],[735,553,553,48,815,637,210,315,692,837,141,101,237,406,540,91,426,256,52,246,496,646,651,308,845,904,623,212,949,647,887,24],[12,256,494,347,54,409,386,461,197,496,416,324,430,932,926,190,663,977,601,415,726,171,810,388,541,773,751,734,4,814,825,561],[809,53,796,710,127,946,706,319,447,207,349,580,783,437,900,466,925,381,562,256,803,933,567,79,10,455,199,170,453,179,276,941],[99,20,206,423,741,273,993,675,827,149,158,530,875,794,832,418,903,496,249,490,868,275,181,164,282,308,179,960,714,492,261,959],[144,600,271,350,131,661,396,819,956,537,147,817,901,767,391,821,498,476,896,53,323,680,585,823,941,550,384,600,853,978,1,152],[23,254,1,762,834,121,816,248,151,211,220,122,111,903,563,359,787,14,639,228,51,161,654,602,747,365,611,24,13,768,588,211],[936,699,986,182,538,403,69,330,321,301,560,177,96,315,315,659,451,354,550,4,652,815,900,287,886,381,85,576,154,222,601,94],[282,203,52,410,429,370,624,320,71,63,990,779,835,331,672,800,726,561,579,594,971,155,783,849,514,410,65,297,926,296,571,996],[906,549,422,907,645,91,617,173,163,298,305,837,109,540,724,71,584,756,102,479,451,219,217,828,934,983,886,736,484,990,923,490],[419,119,475,639,243,31,474,963,894,560,177,858,158,65,99,222,851,583,225,191,876,893,990,788,491,8,774,53,92,547,852,134],[795,981,932,567,168,790,939,562,968,895,744,318,519,142,312,730,155,240,380,109,566,253,277,193,3,661,202,175,939,909,139,174],[236,326,43,848,530,659,541,658,497,916,960,403,153,356,394,710,700,41,128,930,311,777,286,649,115,863,36,877,169,736,570,313],[906,949,446,574,829,46,227,569,700,801,24,534,366,986,684,988,934,820,14,640,246,467,78,405,501,743,967,764,490,554,559,286],[386,140,329,872,382,900,685,547,492,228,251,752,543,285,681,739,521,295,455,769,911,350,16,692,736,48,901,629,715,689,745,225],[423,910,771,160,187,806,399,971,778,665,352,878,825,38,246,842,625,452,635,214,688,274,172,79,209,261,405,320,845,263,457,683],[636,472,193,491,530,722,281,645,350,142,146,821,410,925,919,193,727,890,710,907,673,784,520,846,299,722,833,548,300,532,461,404],[560,813,934,273,654,562,833,896,168,205,609,548,590,484,979,122,839,486,974,254,801,575,951,347,952,78,610,355,562,368,987,734],[151,923,487,649,147,12,972,433,184,519,422,204,646,910,431,748,964,538,814,468,828,182,36,832,222,22,808,214,667,640,219,227],[921,198,337,677,555,140,35,302,618,911,415,830,558,153,888,985,197,112,887,37,285,509,35,18,84,492,565,977,730,254,450,669],[29,466,421,503,507,230,192,901,372,27,793,903,474,987,63,447,730,130,103,415,605,12,606,601,785,691,554,126,134,968,878,927],[180,364,875,762,793,718,127,212,848,140,742,141,598,962,287,481,251,288,885,893,309,860,931,868,138,660,200,911,77,734,902,321],[968,806,427,341,632,983,4,896,343,589,132,734,104,949,968,848,163,861,278,430,944,128,406,967,776,218,276,456,451,915,597,130],[214,367,909,166,586,203,674,90,993,485,388,415,23,522,271,912,425,73,445,508,442,731,381,31,963,230,564,108,256,38,740,68],[332,972,222,688,940,419,126,472,573,395,862,273,719,546,945,626,981,448,636,183,824,999,544,24,342,285,670,564,20,221,93,178],[231,601,816,832,232,894,824,544,99,390,11,283,777,541,68,79,889,168,509,994,471,287,252,455,547,430,746,21,827,111,36,438]]
print(sol.minimumEffortPath(heights))
        