Position BinarySearch(List L, ElementType K)
{
    ElementType left = 1;
    ElementType right = L->Last;
    ElementType mid = 1;
    while(left <= right)
    {
        mid = (left + right) / 2;
        if(L->Data[mid] < K)
        {
            left = mid + 1;
        }
        else if(L->Data[mid] > K)
        {
            right = mid - 1;
        }
        else
        {
            return mid;
        }
    }
    return NotFound;
}