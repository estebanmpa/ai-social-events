import Card from "@/components/Card";
import SearchInput from "@/components/SearchInput";
import useSearch from "@/hooks/useSearch";

export default function SearchPage() {
    const { data, error, loading, fetchData } = useSearch()

    const handleSearch = (value: string) => {
        fetchData(value)
    }

    return (
        <div className="p-2 flex flex-col items-center">
            <h3>Search!</h3>

            <SearchInput className="mt-2" onSearch={handleSearch} />

            {data && <div className="mt-2">
                {data.map(event => {
                    const { title, snippet, link, pagemap } = event
                    const thumbnailSrc = pagemap?.cse_thumbnail?.[0]?.src
                    const imageSrc = pagemap?.cse_image?.[0]?.src
                    const image = thumbnailSrc || imageSrc || undefined
                    return <Card title={title} snippet={snippet} link={link} image={image} className="my-2"/>
                })}
            </div>
            }

        </div>
    )
}